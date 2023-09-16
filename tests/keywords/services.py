from utilities.tests import TestCase
from rest_framework.utils.serializer_helpers import ReturnDict
from parameterized import parameterized
from keywords.services import KeywordServices
from keywords.serializers import KeywordSerializer
from keywords.models import Keyword


DATAS_CREATE_MULTIPLE = [{'name': 'key 4'}, {'name': 'key 3'}]
CASE_CREATE_MULTIPLE = [
    ({'datas': DATAS_CREATE_MULTIPLE, 'return_type': 'instance'}, Keyword),
    ({'datas': DATAS_CREATE_MULTIPLE, 'return_type': 'data'}, ReturnDict),
    (
        {'datas': DATAS_CREATE_MULTIPLE, 'return_type': 'serializer'},
        KeywordSerializer
    ),
]


class keywordServicesTestCase(TestCase):

    @parameterized.expand([({'name': 'key 1'},), ({'name': 'key 2'},),])
    def test_create(self, data):
        serializer = KeywordServices(data=data).create()

        self.assertIsInstance(serializer, KeywordSerializer)

    @parameterized.expand(CASE_CREATE_MULTIPLE)
    def test_create_multiple(self, data_multiple, type_expected):
        return_list = KeywordServices(
            data_multiple=data_multiple
        ).create_multiple()

        self.assertIsInstance(return_list, list)
        self.assertIsInstance(return_list[0], type_expected)
