from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from articles.serializers import Article, ArticleDetailFullSerializer
from articles.services import ArticleServices
from comments.services import CommentServices


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleDetailFullSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'

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

    def destroy(self, request, *args, **kwargs):
        services = ArticleServices(user=request.user)
        services.detail = {'detail': 'Somente um autor pode apagar o artigo.'}

        services.validation_user_author()

        return super().destroy(request, *args, **kwargs)

    def publish(self, request, *args, **kwargs):
        with transaction.atomic():
            response = ArticleServices(
                user=request.user,
                instance=self.get_object(),
                is_publish=kwargs.get('is_publish', False)
            ).publish()

        return Response(response)

    def create_comment(self, request, *args, **kwargs):
        response = CommentServices(
            user=request.user,
            article=self.get_object(),
            data_request=request.data
        ).create()

        return Response(response, status.HTTP_201_CREATED)

    def update_comment(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = CommentServices(
                id=kwargs.get('comment_id'),
                article=self.get_object(),
                data_request=request.data
            ).update()

        return Response(serializer.data)

    def destroy_comment(self, request, *args, **kwargs):
        with transaction.atomic():
            self.get_object()

            CommentServices(id=kwargs.get('id', -1)).destory()

        return Response(status=status.HTTP_204_NO_CONTENT)
