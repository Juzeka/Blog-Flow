from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from articles.serializers import Article, ArticleDetailSerializer
from articles.services import ArticleServices


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        if getattr(self.request.user, 'author', False):
            return Article.objects.filter(author=self.request.user.author)

        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = ArticleServices(
                user=request.user,
                data_request=request.data
            ).create()

        return Response(serializer.data, status.HTTP_201_CREATED)
