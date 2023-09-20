from drf_yasg import openapi


REQUEST_BODY_CREATE_ACCOUNT = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    title='AccountCreate',
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_PASSWORD
        ),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_EMAIL
        ),
        'type': openapi.Schema(type=openapi.TYPE_STRING)
    },
    required=['username', 'password', 'type', 'first_name']
)


REQUEST_BODY_CREATE_ARTICLE = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    title='ArticleCreate',
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING),
        'subtitle': openapi.Schema(type=openapi.TYPE_STRING),
        'content': openapi.Schema(type=openapi.TYPE_STRING),
        'category': openapi.Schema(type=openapi.TYPE_INTEGER),
        'keywords': openapi.Schema(
            type=openapi.TYPE_STRING,
            items=None,
            example=[{"name": "value"}]
        ),
    },
    required=['title', 'subtitle', 'content', 'category', 'keywords']
)


REQUEST_BODY_UPDATE_ARTICLE = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    title='ArticleUpdate',
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING),
        'subtitle': openapi.Schema(type=openapi.TYPE_STRING),
        'content': openapi.Schema(type=openapi.TYPE_STRING),
        'category': openapi.Schema(type=openapi.TYPE_INTEGER),
        'keywords': openapi.Schema(
            type=openapi.TYPE_STRING,
            items=None,
            example=[
                {"id": 1, "name": "value"},
                {"id": 2, "destroy": True},
                {"name": "value"}
            ]
        ),
    }
)


REQUEST_BODY_PUBLISH_ARTICLE = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    title='ArticlePublish',
    properties={
        'is_publish': openapi.Schema(type=openapi.TYPE_BOOLEAN, default=False)
    }
)


REQUEST_BODY_CREATE_COMMENT = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    title='CommentCreate',
    properties={
        'content': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['content']
)


REQUEST_BODY_UPDATE_COMMENT = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    title='CommentUpdate',
    properties={
        'content': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['content']
)


REQUEST_BODY_CHANGE_STATUS_COMMENT = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    title='CommentChangeStatus',
    properties={
        'status': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['status']
)


REQUEST_BODY_CREATE_CATEGORY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    title='CategoryCreate',
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['name']
)
