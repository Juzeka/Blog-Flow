import factory
from accounts.factories import UserFactory
from author.models import Author


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    user = factory.SubFactory(UserFactory)
