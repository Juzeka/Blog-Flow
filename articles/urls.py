from django.urls import path
from articles.views import ArticleViewSet


urlpatterns = [
    path(
        '',
        ArticleViewSet.as_view(actions={'post': 'create', 'get': 'list'})
    ),
    path(
        '<int:id>/publish/',
        ArticleViewSet.as_view(actions={'post': 'publish'})
    ),
    path(
        '<int:id>/comments/',
        ArticleViewSet.as_view(actions={'post': 'create_comment'})
    ),
]
