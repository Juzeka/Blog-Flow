from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from author.serializers import Author, AuthorSerializer


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
