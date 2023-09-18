from utilities.tests import BaseViewTestCase
from rest_framework.exceptions import NotFound
from parameterized import parameterized
from accounts.factories import UserFactory
from articles.factories import ArticleFactory
from comments.services import CommentServices
from comments.factories import CommentFactory
from comments.serializers import CommentSerializer
from utilities.choices import APPROVED_CHOICE


TESTE_CASE_UPDATE = [({'content': 'conteudo update'},), ({},),]


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

    @parameterized.expand(TESTE_CASE_UPDATE)
    def test_update(self, data):
        comment = CommentFactory()

        result = CommentServices(
            id=comment.id,
            article=comment.article,
            data_request=data
        ).update()

        self.assertIsInstance(result, CommentSerializer)

    def test_destory(self):
        comment = CommentFactory()

        result = CommentServices(id=comment.id).destory()

        self.assertIsNone(result)

    def test_destory_exception(self):
        try:
            CommentServices(id=-1).destory()
        except NotFound as e:
            detail = e.detail['detail'].capitalize()

            self.assertEqual(detail, 'Comentário não encotrado.')

    def test_change_status(self):
        comment = CommentFactory()

        result = CommentServices(
            article=comment.article,
            id=comment.id,
            data_request={'status': APPROVED_CHOICE}
        ).change_status()

        self.assertIsInstance(result, CommentSerializer)
