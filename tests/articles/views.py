from utilities.tests import BaseViewTestCase
from rest_framework import status
from parameterized import parameterized
from accounts.factories import UserFactory
from author.factories import AuthorFactory
from categories.factories import CategoryFactory
from articles.factories import ArticleFactory
from comments.factories import CommentFactory
from keywords.factories import KeywordFactory


TEST_CASE_CREATE_EXCEPTION = [
    ({}, False, status.HTTP_403_FORBIDDEN),
    ({}, True, status.HTTP_400_BAD_REQUEST),
]
TEST_CASE_PUBLISH = [(True,), (False),]
TESTE_CASE_UPDATE = [({'content': 'conteudo update'},), ({},),]
TESTE_CASE_UPDATE_ARTICLE = [
    ({'title': 'editando titulo'}, False),
    ({'title': 'editando titulo 2', 'subtitle': 'editando subtitle'}, False),
    (
        {
            'keywords': [
                {'name': 'Nova key'},
                {'id': 99, 'name': 'editando key'},
                {'id': -1, 'name': 'nova key apartir de um id inexistente'},
                {'id': 98, 'destroy': True}
            ]
        },
        True
    )
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

    def base_destroy(self, is_author=True):
        article = ArticleFactory()
        username = article.author.user if is_author else UserFactory()

        self.get_token(username=username.username, password='password123')

        return self.client.delete(
            path=f'{self.base_router}/{article.id}/',
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

    @parameterized.expand(TEST_CASE_PUBLISH)
    def test_publish(self, is_publish):
        instance = ArticleFactory()

        self.get_token(
            username=instance.author.user.username,
            password='password123'
        )

        response = self.client.post(
            path=f'{self.base_router}/{instance.id}/publish/',
            data={'is_publish': is_publish},
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_publish_exception(self):
        instance = ArticleFactory()

        self.get_token(username=UserFactory().username, password='password123')

        response = self.client.post(
            path=f'{self.base_router}/{instance.id}/publish/',
            data={'is_publish': ''},
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list(self):
        user = UserFactory()
        author = AuthorFactory(user=user)
        articles = ArticleFactory.create_batch(size=3, author=author)

        self.get_token(username=user.username, password='password123')

        response = self.client.get(path=f'{self.base_router}/', **self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], len(articles))

    def test_retrieve(self):
        article = ArticleFactory()

        self.get_token(
            username=article.author.user.username,
            password='password123'
        )

        response = self.client.get(
            path=f'{self.base_router}/{article.id}/',
            **self.headers
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destory(self):
        response = self.base_destroy()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_destory_exception(self):
        response = self.base_destroy(is_author=False)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_comment(self):
        user = UserFactory()
        article = ArticleFactory()

        self.get_token(username=user.username, password='password123')

        response = self.client.post(
            path=f'{self.base_router}/{article.id}/comments/',
            data={'content': 'Comentário 2'},
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @parameterized.expand(TESTE_CASE_UPDATE)
    def test_update_comment(self, data):
        article = ArticleFactory()
        comment = CommentFactory(article=article, user=article.author.user)

        self.get_token(
            username=article.author.user.username,
            password='password123'
        )

        response = self.client.patch(
            path=f'{self.base_router}/{article.id}/comments/{comment.id}/',
            data=data,
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @parameterized.expand(TESTE_CASE_UPDATE_ARTICLE)
    def test_update(self, data, is_keywords):
        article = ArticleFactory()

        if is_keywords:
            KeywordFactory(id=99)
            KeywordFactory(id=98)

        self.get_token(
            username=article.author.user.username,
            password='password123'
        )

        response = self.client.put(
            path=f'{self.base_router}/{article.id}/',
            data=data,
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
