from rest_framework.exceptions import NotFound
from utilities.choices import WAITING_APPROVED_CHOICE
from comments.serializers import CommentSerializer, CommentContentSerializer
from comments.models import Comment
from utilities.tasks import trigger_task, notify_email


class CommentServices:
    def __init__(self, *args, **kwargs) -> None:
        self.user = kwargs.get('user')
        self.id = kwargs.get('id')
        self.article = kwargs.get('article')
        self.data_request = kwargs.get('data_request')
        self.instance = None

    def get_object(self, params):
        try:
            self.instance = Comment.objects.get(**params)
            return self.instance
        except Comment.DoesNotExist:
            raise NotFound(detail={'detail': 'Comentário não encotrado.'})

    def retrieve(self):
        serializer = CommentSerializer(
            instance=self.get_object(
                params={'id': self.id, 'article': self.article}
            )
        )

        return serializer

    def create(self):
        data = {
            **self.data_request,
            'user': self.user.id,
            'article': self.article.id
        }
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        detail = {
            'detail': 'Comentário enviado com sucesso, sujeito à aprovação.'
        }

        if self.user.email:
            params = {
                'subject': 'Novo artigo',
                'message': '''
                    Seu artigo foi criado com sucesso e está pronto para ser
                    publicado.
                ''',
                'from_email': 'no-reply@blogflow.com',
                'recipient_list': [self.user.email]
            }

            trigger_task(task=notify_email, kwargs=params)

        return detail

    def update(self):
        instance = self.get_object(
            params={'id': self.id, 'article': self.article.id}
        )
        content_serializer = CommentContentSerializer(data=self.data_request)
        is_valid = content_serializer.is_valid()

        if is_valid:
            data = {
                **content_serializer.data,
                'status': WAITING_APPROVED_CHOICE
            }

            serializer = CommentSerializer(
                instance=instance,
                data=data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            serializer = CommentSerializer(instance=instance)

        return serializer

    def destory(self):
        instance = self.get_object(params={'id': self.id})
        instance.delete()

    def change_status(self):
        instance = self.get_object(
            params={'id': self.id, 'article': self.article}
        )

        serializer = CommentSerializer(
            instance=instance,
            data={'status': self.data_request.get('status')},
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer
