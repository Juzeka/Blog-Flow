from django.test import TestCase


class BaseViewTestCase(TestCase):
    def get_token(self, username, password):
        response = self.client.post(
            '/api/v1/accounts/auth/token/',
            data={
                'username': username,
                'password': password
            }
        )

        self.tokens = response.data
        self.headers = {
            'HTTP_AUTHORIZATION': f'Bearer {self.tokens.get("access")}'
        }

        return self.tokens
