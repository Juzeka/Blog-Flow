from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


prefix_v1 = 'api/v1'
schema_view = get_schema_view(
   openapi.Info(
      title='Documentação',
      default_version='v1',
      description='Lista de endpoints',
      contact=openapi.Contact(email='rafaelgomesalmeida@hotmail.com'),
   ),
   public=True,
)

urlpatterns = [
    path(f'{prefix_v1}/accounts/', include('accounts.urls')),
    path(f'{prefix_v1}/articles/', include('articles.urls')),
    path(f'{prefix_v1}/categories/', include('categories.urls')),
    path(f'{prefix_v1}/doc/', schema_view.with_ui()),
    path('', admin.site.urls),
]
