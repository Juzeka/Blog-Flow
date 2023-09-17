from utilities.tests import BaseViewTestCase
from rest_framework.exceptions import PermissionDenied, ValidationError
from parameterized import parameterized
from articles.serializers import ArticleSerializer
from articles.services import ArticleServices
from categories.factories import CategoryFactory
from author.factories import AuthorFactory
from accounts.factories import UserFactory
from articles.factories import ArticleFactory


TEST_CASE_CREATE = [
    ({
        'title': 'Titulo 1',
        'subtitle': 'Subtitulo 1',
        'content': 'Conteudo 1',
        'keywords': [{'name': 'key 1'}, {'name': 'key 2'}]
    },),
    ({
        'title': 'Titulo 2',
        'subtitle': 'Subtitulo 2',
        'content': 'Conteudo 2',
        'keywords': [{'name': 'key 3'}, {'name': 'key 4'}]
    },),
]
TEST_CASE_PUBLISH = [
    (True, 'Artigo publicado com sucesso.'),
    (False, 'Artigo não foi aprovado.')
]


class ArticleServicesTestCase(BaseViewTestCase):
    def base_create(self, data, user):
        data.update({'category': CategoryFactory().id})

        return ArticleServices(user=user, data_request=data).create()

    @parameterized.expand(TEST_CASE_CREATE)
    def test_create(self, data):
        result = self.base_create(data=data, user=AuthorFactory().user)

        self.assertIsInstance(result, ArticleSerializer)

    def test_exception_validation_user_author(self):
        try:
            self.base_create(data=dict(), user=UserFactory())
        except PermissionDenied as e:
            detail = e.detail['detail'].capitalize()

            self.assertEqual(detail, 'Somente um autor pode criar um artigo.')

    def test_exception_validation_keywords_in_data_request(self):
        try:
            self.base_create(data=dict(), user=AuthorFactory().user)
        except ValidationError as e:
            detail = e.detail['detail'].capitalize()

            self.assertEqual(detail, 'O campo keywords é obrigatório.')

    @parameterized.expand(TEST_CASE_PUBLISH)
    def test_publish(self, is_publish, detail):
        instance = ArticleFactory()

        result = ArticleServices(
            instance=instance,
            user=AuthorFactory().user,
            is_publish=is_publish
        ).publish()

        self.assertEqual(result['detail'], detail)

    def test_publish_exception(self):
        try:
            ArticleServices(
                user=UserFactory(),
            ).publish()
        except PermissionDenied as e:
            detail = e.detail['detail'].capitalize()

            self.assertEqual(detail, 'Somente um autor pode publicar o artigo.')
