from utilities.tests import TestCase
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.exceptions import ValidationError
from parameterized import parameterized
from keywords.services import KeywordServices
from keywords.serializers import KeywordSerializer
from keywords.models import Keyword


DATAS_CREATE_MULTIPLE = [{'name': 'key 4'}, {'name': 'key 3'}]
CASE_CREATE_MULTIPLE = [
    ({'datas': DATAS_CREATE_MULTIPLE, 'return_type': 'instance'}, Keyword),
    ({'datas': DATAS_CREATE_MULTIPLE, 'return_type': 'data'}, ReturnDict),
    ({'datas': DATAS_CREATE_MULTIPLE, 'return_type': 'id'}, int),
    (
        {'datas': DATAS_CREATE_MULTIPLE, 'return_type': 'serializer'},
        KeywordSerializer
    ),
]
TEST_CASE_EXCEPTION_VALIDATION = [
    ({'datas': [1, 2]}, 'Formato do keyword incorreto, tente: {"name": "value"}'),
    ({'datas': DATAS_CREATE_MULTIPLE, 'return_type': 'test'}, 'Tipo de retorno incorreto.'),
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

    @parameterized.expand(TEST_CASE_EXCEPTION_VALIDATION)
    def test_exception_validation_format_datas_in_data_multiple(self, data, msg):
        try:
            KeywordServices(data_multiple=data).create_multiple()
        except ValidationError as e:
            detail = e.detail['detail'].capitalize()

            self.assertEqual(detail, msg)
