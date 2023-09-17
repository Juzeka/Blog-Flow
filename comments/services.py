from comments.serializers import CommentSerializer


class CommentServices:
    def __init__(self, *args, **kwargs) -> None:
        self.user = kwargs.get('user')
        self.article = kwargs.get('article')
        self.data_request = kwargs.get('data_request')

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

        return detail
