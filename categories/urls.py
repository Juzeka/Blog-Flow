from django.urls import path
from categories.views import CategoryViewSet


urlpatterns = [
    path(
        '',
        CategoryViewSet.as_view(actions={'post': 'create', 'get': 'list'})
    ),
    path(
        '<int:id>/',
        CategoryViewSet.as_view(
            actions={'delete': 'destroy', 'get': 'retrieve', 'put': 'update'}
        )
    ),
]
