from django.db import transaction
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from accounts.services import AccountServices
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from core.schema_parameters import REQUEST_BODY_CREATE_ACCOUNT
from core.schema_responses import (
    RESPONSE_CREATE_ACCOUNT,
)


class CreateAccountViewSet(ViewSet):
    authentication_classes = []
    permission_classes = []
    services_class = AccountServices

    @swagger_auto_schema(
        tags=['Accounts'],
        operation_id='account_create',
        operation_summary='Criação de uma nova conta',
        request_body=REQUEST_BODY_CREATE_ACCOUNT,
        responses=RESPONSE_CREATE_ACCOUNT
    )
    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            self.services_class(
                data_request=request.data
            ).create_user()

        response = {'detail': 'Conta criada com sucesso.'}

        return Response(data=response, status=status.HTTP_201_CREATED)


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        tags=['Accounts'],
        operation_id='account_token_get',
        operation_summary='Gera token de acesso para o usuário.',
    ),
)
class TokenObtainPairView(TokenObtainPairView): pass


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        tags=['Accounts'],
        operation_id='account_token_refresh',
        operation_summary='Atualiza o token de acesso para o usuário.',
    ),
)
class TokenRefreshView(TokenRefreshView): pass
