from django.views.decorators.cache import cache_page
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from categories.serializers import Category, CategorySerializer
from core.schema_parameters import REQUEST_BODY_CREATE_CATEGORY


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        tags=['Categories'],
        operation_id='categories_list',
        operation_summary='Listagem de categorias.',
    )
)
@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        tags=['Categories'],
        operation_id='categories_create',
        operation_summary='Criação de artigo.',
        request_body=REQUEST_BODY_CREATE_CATEGORY
    )
)
@method_decorator(name='list', decorator=cache_page(60 * 10))
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)
