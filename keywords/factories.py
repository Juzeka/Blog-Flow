import factory
from keywords.models import Keyword


class KeywordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Keyword

    name = factory.Sequence(lambda n: 'key %d' % n)
