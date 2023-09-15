from django.db import transaction
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from accounts.services import AccountServices


class CreateAccountViewSet(ViewSet):
    authentication_classes = []
    permission_classes = []
    services_class = AccountServices

    def get_serializer(self):
        return

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            self.services_class(
                data_request=request.data
            ).create_user()

        response = {'detail': 'Conta criado com sucesso.'}

        return Response(data=response, status=status.HTTP_201_CREATED)
