from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from categories.serializers import Category, CategorySerializer


@method_decorator(name='list', decorator=cache_page(60 * 10))
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)
