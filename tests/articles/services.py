from utilities.tests import BaseViewTestCase
from parameterized import parameterized
from articles.serializers import ArticleSerializer
from articles.services import ArticleServices
from categories.factories import CategoryFactory
from author.factories import AuthorFactory


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


class ArticleServicesTestCase(BaseViewTestCase):

    @parameterized.expand(TEST_CASE_CREATE)
    def test_create(self, data):
        category = CategoryFactory()
        author = AuthorFactory()

        data.update({'category': category.id})

        result = ArticleServices(user=author.user, data_request=data).create()

        self.assertIsInstance(result, ArticleSerializer)
