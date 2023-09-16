from django.urls import path
from categories.views import CategoryViewSet


urlpatterns = [
    path('', CategoryViewSet.as_view(actions={'post': 'create'}))
]
