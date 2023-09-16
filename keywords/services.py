from rest_framework.exceptions import ValidationError
from keywords.serializers import (
    KeywordSerializer,
    KeywordMultipleSerializer
)


class KeywordServices:
    def __init__(self, *args, **kwargs) -> None:
        self.data_multiple = kwargs.get('data_multiple')
        self.data = kwargs.get('data')
        self.serializer = None

    def validation_format_datas_in_data_multiple(self):
        serializer = KeywordMultipleSerializer(data=self.data_multiple)
        is_valid = serializer.is_valid()
        detail = {
            'detail': 'Formato do keyword incorreto, tente: {"name": "value"}'
        }

        if not is_valid:
            if serializer.errors.get('return_type', False):
                detail = {'detail': 'Tipo de retorno incorreto.'}

            raise ValidationError(detail=detail)

        self.serializer = serializer

    def create(self):
        serializer = KeywordSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer

    def create_multiple(self):
        self.validation_format_datas_in_data_multiple()

        list_data = self.serializer.data['datas']
        return_type = self.serializer.data['return_type']
        return_list = list()

        for data in list_data:
            self.data = data
            result = self.create()

            if return_type == 'instance':
                result = result.instance
            elif return_type == 'id':
                result = result.instance.id
            elif return_type == 'data':
                result = result.data

            return_list.append(result)

        return return_list
