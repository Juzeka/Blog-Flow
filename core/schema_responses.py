from drf_yasg import openapi
from rest_framework import status


RESPONSE_CREATE_ACCOUNT = {
    status.HTTP_201_CREATED: openapi.Schema(
        title='AccountCreated',
        type=openapi.TYPE_OBJECT,
        properties={
            'detail': openapi.Schema(
                type=openapi.TYPE_STRING,
                default='Conta criada com sucesso.'
            )
        }
    )
}


RESPONSE_CREATE_ARTICLE = {
    status.HTTP_201_CREATED: openapi.Schema(
        title='ArticleCreated',
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'category': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'name': openapi.Schema(type=openapi.TYPE_STRING)
                }
            ),
            'keywords': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'updated_at': openapi.Schema(
                            type=openapi.TYPE_NUMBER,
                            format=openapi.FORMAT_DATETIME
                        ),
                        'created_at': openapi.Schema(
                            type=openapi.TYPE_NUMBER,
                            format=openapi.FORMAT_DATETIME
                        ),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN)
                    }
                )
            ),
            'updated_at': openapi.Schema(
                type=openapi.TYPE_NUMBER,
                format=openapi.FORMAT_DATETIME
            ),
            'created_at': openapi.Schema(
                type=openapi.TYPE_NUMBER,
                format=openapi.FORMAT_DATETIME
            ),
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'subtitle': openapi.Schema(type=openapi.TYPE_STRING),
            'content': openapi.Schema(type=openapi.TYPE_STRING),
            'status': openapi.Schema(type=openapi.TYPE_STRING),
            'is_visible': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            'author': openapi.Schema(type=openapi.TYPE_INTEGER)
        }
    )
}
