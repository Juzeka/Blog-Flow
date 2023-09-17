import factory
from comments.models import Comment
from accounts.factories import UserFactory
from articles.factories import ArticleFactory


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    user = factory.SubFactory(UserFactory)
    article = factory.SubFactory(ArticleFactory)
    content = factory.Sequence(lambda n: 'conteudo %d' % n)
