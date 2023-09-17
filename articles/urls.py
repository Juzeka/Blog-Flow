from django.urls import path
from articles.views import ArticleViewSet


urlpatterns = [
    path(
        '',
        ArticleViewSet.as_view(actions={'post': 'create', 'get': 'list'})
    ),
    path(
        '<int:id>/',
        ArticleViewSet.as_view(
            actions={'get': 'retrieve', 'delete': 'destroy'}
        )
    ),
    path(
        '<int:id>/publish/',
        ArticleViewSet.as_view(actions={'post': 'publish'})
    ),
    path(
        '<int:id>/comments/',
        ArticleViewSet.as_view(actions={'post': 'create_comment'})
    ),
    path(
        '<int:id>/comments/<int:comment_id>/',
        ArticleViewSet.as_view(
            actions={'patch': 'update_comment', 'delete': 'destory'}
        )
    ),
]
