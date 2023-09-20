from django.db import transaction
from django.views.decorators.cache import cache_page
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from articles.serializers import Article, ArticleDetailFullSerializer
from articles.services import ArticleServices
from comments.services import CommentServices
from core.schema_parameters import (
    REQUEST_BODY_CREATE_ARTICLE,
    REQUEST_BODY_UPDATE_ARTICLE,
    REQUEST_BODY_PUBLISH_ARTICLE,
    REQUEST_BODY_CREATE_COMMENT,
    REQUEST_BODY_UPDATE_COMMENT,
    REQUEST_BODY_CHANGE_STATUS_COMMENT
)
from core.schema_responses import RESPONSE_CREATE_ARTICLE


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        tags=['Articles'],
        operation_id='accounts_list',
        operation_summary='Listagem de artigos.',
    )
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        tags=['Articles'],
        operation_id='accounts_retrieve',
        operation_summary='Detalhe de artigos.',
    )
)
@method_decorator(
    name='publish',
    decorator=swagger_auto_schema(
        tags=['Articles'],
        operation_id='accounts_publish',
        operation_summary='Publicação de artigo.',
        request_body=REQUEST_BODY_PUBLISH_ARTICLE
    )
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        tags=['Articles'],
        operation_id='accounts_destroy',
        operation_summary='Deleção de artigo.',
    ),
)
@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        tags=['Articles'],
        operation_id='accounts_create',
        operation_summary='Criação de artigo.',
        request_body=REQUEST_BODY_CREATE_ARTICLE,
        responses=RESPONSE_CREATE_ARTICLE
    ),
)
@method_decorator(
    name='update',
    decorator=swagger_auto_schema(
        tags=['Articles'],
        operation_id='accounts_update',
        operation_summary='Edição de artigo.',
        request_body=REQUEST_BODY_UPDATE_ARTICLE,
        responses=RESPONSE_CREATE_ARTICLE
    ),
)
@method_decorator(
    name='create_comment',
    decorator=swagger_auto_schema(
        tags=['Comments'],
        operation_id='accounts_comments_create',
        operation_summary='Criação de comentário.',
        request_body=REQUEST_BODY_CREATE_COMMENT
    )
)
@method_decorator(
    name='update_comment',
    decorator=swagger_auto_schema(
        tags=['Comments'],
        operation_id='accounts_comments_update',
        operation_summary='Edição de comentário.',
        request_body=REQUEST_BODY_UPDATE_COMMENT
    )
)
@method_decorator(
    name='destroy_comment',
    decorator=swagger_auto_schema(
        tags=['Comments'],
        operation_id='accounts_comments_destroy',
        operation_summary='Deleção de comentário.',
    )
)
@method_decorator(
    name='change_status_comment',
    decorator=swagger_auto_schema(
        tags=['Comments'],
        operation_id='accounts_comments_change_status',
        operation_summary='Alteração do status de comentário.',
        request_body=REQUEST_BODY_CHANGE_STATUS_COMMENT
    )
)
@method_decorator(
    name='retrieve_comment',
    decorator=swagger_auto_schema(
        tags=['Comments'],
        operation_id='accounts_comments_retrieve',
        operation_summary='Detalhe do comentário.'
    )
)
@method_decorator(name='list', decorator=cache_page(60 * 10))
@method_decorator(name='retrieve', decorator=cache_page(60 * 10))
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

    def update(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = ArticleServices(
                user=request.user,
                instance=self.get_object(),
                data_request=request.data
            ).update()

        return Response(serializer.data)

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
                is_publish=request.data.get('is_publish', False)
            ).publish()

        return Response(response)

    def create_comment(self, request, *args, **kwargs):
        response = CommentServices(
            user=request.user,
            article=self.get_object(),
            data_request=request.data
        ).create()

        return Response(response, status.HTTP_201_CREATED)

    def retrieve_comment(self, request, *args, **kwargs):
        serializer = CommentServices(
            id=kwargs.get('id', -1),
            article=self.get_object()
        ).retrieve()

        return Response(serializer.data)

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

            CommentServices(id=kwargs.get('comment_id', -1)).destory()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def change_status_comment(self, request, *args, **kwargs):
        serializer = CommentServices(
            article=self.get_object(),
            id=kwargs.get('comment_id', -1),
            data_request=request.data
        )

        return Response(serializer.data)
