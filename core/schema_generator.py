from drf_yasg.generators import OpenAPISchemaGenerator
from django.conf import settings


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        swagger = super().get_schema(request, public)

        swagger.schemes = ['http'] if settings.DEBUG else ['https', 'http']
        swagger.tags = [
            {
                'name': 'Accounts',
                'description': 'Gerenciamento de contas.',
            },
            {
                'name': 'Articles',
                'description': 'Gerenciamento dos artigos.',
            },
            {
                'name': 'Comments',
                'description': 'Gerenciamento dos comentários.',
            },
            {
                'name': 'Categories',
                'description': 'Gerenciamento das categorias.',
            }

        ]

        return swagger
