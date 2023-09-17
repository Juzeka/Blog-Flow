from django.urls import path
from articles.views import ArticleViewSet


urlpatterns = [
    path('', ArticleViewSet.as_view(actions={'post': 'create'})),
    path(
        '<int:id>/publish/',
        ArticleViewSet.as_view(actions={'post': 'publish'})
    )
]
