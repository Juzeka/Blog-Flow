import factory
from articles.models import Article
from author.factories import AuthorFactory
from categories.factories import CategoryFactory
from keywords.factories import KeywordFactory


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Sequence(lambda n: 'Titulo %s' % n)
    title = factory.Sequence(lambda n: 'Subtitulo %s' % n)
    content = factory.Sequence(lambda n: 'Conteudo %s' % n)
    author = factory.SubFactory(AuthorFactory)
    category = factory.SubFactory(CategoryFactory)
    keywords = factory.RelatedFactoryList(KeywordFactory, size=2)
