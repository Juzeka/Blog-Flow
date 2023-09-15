from rest_framework.viewsets import ModelViewSet
from categories.serializers import Category, CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)
