from utilities.tests import BaseViewTestCase
from accounts.factories import UserFactory


class CategoryViewSetTestCase(BaseViewTestCase):
    def setUp(self) -> None:
        self.user_1 = UserFactory()


