from utilities.tests import BaseViewTestCase
from accounts.factories import UserFactory
from articles.factories import ArticleFactory
from comments.services import CommentServices


class CommentServicesTestCase(BaseViewTestCase):
    def setUp(self) -> None:
        self.user_1 = UserFactory()

    def test_create(self):
        detail = 'Comentário enviado com sucesso, sujeito à aprovação.'
        self.get_token(username=self.user_1, password='password123')

        result = CommentServices(
            user=self.user_1,
            article=ArticleFactory(),
            data_request={'content': 'Comentário 1'}
        ).create()

        self.assertEqual(result['detail'], detail)
