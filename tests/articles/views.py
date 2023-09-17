from utilities.tests import BaseViewTestCase
from rest_framework import status
from parameterized import parameterized
from accounts.factories import UserFactory
from author.factories import AuthorFactory
from categories.factories import CategoryFactory
from articles.factories import ArticleFactory
from comments.factories import CommentFactory


TEST_CASE_CREATE_EXCEPTION = [
    ({}, False, status.HTTP_403_FORBIDDEN),
    ({}, True, status.HTTP_400_BAD_REQUEST),
]
TEST_CASE_PUBLISH = [(True,), (False),]
TESTE_CASE_UPDATE = [({'content': 'conteudo update'},), ({},),]


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
    def test_update(self, data):
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
