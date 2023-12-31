from rest_framework.viewsets import ModelViewSet
from author.serializers import Author, AuthorSerializer


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
