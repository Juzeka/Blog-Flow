from utilities.tests import TestCase
from parameterized import parameterized
from keywords.services import KeywordServices
from keywords.serializers import KeywordSerializer


class keywordServicesTestCase(TestCase):

    @parameterized.expand([({'name': 'key 1'},), ({'name': 'key 2'},),])
    def test_create(self, data):
        serializer = KeywordServices(data=data).create()

        self.assertIsInstance(serializer, KeywordSerializer)
