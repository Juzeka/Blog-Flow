from articles.serializers import ArticleSerializer, ArticleDetailSerializer
from rest_framework.exceptions import PermissionDenied, ValidationError
from keywords.services import KeywordServices
from utilities.choices import PUBLISHED_CHOICE, CANCELED_CHOICE


class ArticleServices:
    def __init__(self, *args, **kwargs) -> None:
        self.user = kwargs.get('user')
        self.data_request = kwargs.get('data_request')
        self.instance = kwargs.get('instance')
        self.is_publish = kwargs.get('is_publish')
        self.detail = None

    def validation_keywords_in_data_request(self):
        detail = {'detail': 'O campo keywords é obrigatório.'}

        if not self.data_request.get('keywords', False):
            raise ValidationError(detail=detail)

    def validation_user_author(self):
        detail = {'detail': 'Somente um autor pode criar um artigo.'}

        if not getattr(self.user, 'author', False):
            raise PermissionDenied(
                detail=self.detail if self.detail else detail
            )

    def create(self):
        self.validation_user_author()
        self.validation_keywords_in_data_request()

        data_multiple = {
            'datas': self.data_request.get('keywords', list()),
            'return_type': 'id'
        }
        keywords = KeywordServices(
            data_multiple=data_multiple
        ).create_multiple()

        data = {
            **self.data_request,
            'author': self.user.author.id,
            'keywords': keywords
        }
        serializer = ArticleSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return ArticleDetailSerializer(instance=serializer.instance)

    def publish(self):
        self.detail = {'detail': 'Somente um autor pode publicar o artigo.'}
        self.validation_user_author()

        data = {'status': CANCELED_CHOICE}
        msg = 'Artigo não foi aprovado.'

        if self.is_publish:
            msg = 'Artigo publicado com sucesso.'
            data.update({'status': PUBLISHED_CHOICE, 'is_visible': True})

        serializer = ArticleSerializer(
            instance=self.instance,
            data=data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return {'detail': msg}
