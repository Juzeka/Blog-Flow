from utilities.tests import BaseViewTestCase
from parameterized import parameterized
from rest_framework import status
from accounts.factories import UserFactory


TEST_CASE_CREATE = [({'name': 'category 1'},), ({'name': 'category 2'},)]


class CategoryViewSetTestCase(BaseViewTestCase):
    base_router = '/api/v1/categories'

    def setUp(self) -> None:
        self.user = UserFactory()

    @parameterized.expand(TEST_CASE_CREATE)
    def test_create(self, data):
        self.get_token(username=self.user.username, password='password123')

        response = self.client.post(
            path=f'{self.base_router}/',
            data=data,
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
