from utilities.tests import BaseViewTestCase
from rest_framework import status
from parameterized import parameterized
from rest_framework.exceptions import PermissionDenied, ValidationError
from accounts.factories import UserFactory
from author.factories import AuthorFactory
from categories.factories import CategoryFactory


TEST_CASE_CREATE_EXCEPTION = [
    ({}, False, status.HTTP_403_FORBIDDEN),
    ({}, True, status.HTTP_400_BAD_REQUEST),
]


class ArticleViewSetTestCase(BaseViewTestCase):
    base_router = '/api/v1/articles'

    def setUp(self) -> None:
        self.category = CategoryFactory()

    def base_create(self, username, data):
        self.get_token(
            username=username,
            password='password123'
        )

        return self.client.post(
            path=f'{self.base_router}/',
            data=data,
            content_type='application/json',
            **self.headers
        )

    def test_create(self):
        data = {
            'title': 'Titulo 1',
            'subtitle': 'Subtitulo 1',
            'content': 'Conteudo 1',
            'category': self.category.pk,
            'keywords': [{'name': 'key 1'}, {'name': 'key 2'}]
        }

        response = self.base_create(
            username=AuthorFactory().user.username,
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @parameterized.expand(TEST_CASE_CREATE_EXCEPTION)
    def test_create_exception(self, data, is_author, expected):
        user = AuthorFactory().user if is_author else UserFactory()

        response = self.base_create(username=user.username, data=data)

        self.assertEqual(response.status_code, expected)
