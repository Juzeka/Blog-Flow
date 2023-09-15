from rest_framework import status
from utilities.tests import BaseViewTestCase
from accounts.factories import UserFactory
from parameterized import parameterized


class AccountsViewsetTestCase(BaseViewTestCase):
    base_router = '/api/v1/accounts'

    def setUp(self) -> None:
        self.password_1 = 'PassTest'
        self.user_1 = UserFactory(password=self.password_1)

    def test_login(self):
        data = {'username': self.user_1.username, 'password': self.password_1}

        response = self.client.post(
            path=f'{self.base_router}/auth/token/',
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('access'))
        self.assertTrue(response.data.get('refresh'))

    def test_refresh_token(self):
        tokens = self.get_token(
            username=self.user_1.username,
            password=self.password_1
        )

        response = self.client.post(
            path=f'{self.base_router}/auth/token/refresh/',
            data={'refresh': tokens['refresh']},
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['access'] != tokens['access'])

    @parameterized.expand([('Test_1', 'author'), ('Test_2', 'user')])
    def test_create_account(self, username, type_user):
        data_create = {
            'username': username,
            'password': 'teste',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'type': type_user
        }

        response = self.client.post(
            path=f'{self.base_router}/',
            data=data_create,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['detail'], 'Conta criada com sucesso.')
