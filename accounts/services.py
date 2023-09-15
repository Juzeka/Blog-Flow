from accounts.serializers import UserSerializer, CreateAccountSerializer
from author.serializers import AuthorSerializer


class AccountServices:
    def __init__(self, *args, **kwargs) -> None:
        self.data_request = kwargs.get('data_request', None)
        self.data_create = None
        self.instance_user = None

    def validate_data_create(self):
        self.data_create = CreateAccountSerializer(data=self.data_request)
        self.data_create.is_valid(raise_exception=True)

    def create_author(self):
        if self.data_create.data['type'] == 'author':
            serializer = AuthorSerializer(data={'user': self.instance_user.pk})
            serializer.is_valid(raise_exception=True)
            serializer.save()

    def create_user(self):
        data = {**self.data_request, 'is_staff': True}

        self.validate_data_create()

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.instance_user = serializer.instance

        self.create_author()

        return serializer
