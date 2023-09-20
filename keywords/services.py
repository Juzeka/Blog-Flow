from rest_framework.exceptions import ValidationError
from keywords.serializers import (
    KeywordSerializer,
    KeywordMultipleSerializer,
    KeywordUpdateMultipleSerializer
)
from keywords.models import Keyword


class KeywordServices:
    def __init__(self, *args, **kwargs) -> None:
        self.instance = kwargs.get('instance')
        self.data_multiple = kwargs.get('data_multiple')
        self.datas = kwargs.get('datas')
        self.data = kwargs.get('data')
        self.queryset = kwargs.get('queryset')
        self.serializer = None
        self.type = None

    def validation_format_datas_in_data_multiple(self):
        serializer = KeywordMultipleSerializer(data=self.data_multiple)
        is_valid = serializer.is_valid()

        msg = 'Formato do keyword incorreto, tente: [{"name": "value"}]'
        detail = {'detail': msg}

        if not is_valid:
            if serializer.errors.get('return_type', False):
                detail = {'detail': 'Tipo de retorno incorreto.'}

            raise ValidationError(detail=detail)

        self.serializer = serializer

    def return_type(self, serializer):
        result = serializer

        if self.type == 'instance':
            result = serializer.instance
        elif self.type == 'id':
            result = serializer.instance.id
        elif self.type == 'data':
            result = serializer.data

        return result

    def concat_list_keywords_with_existing(self, new_keys:list):
        serializer = KeywordSerializer(self.queryset, many=True)

        existing = [data['id'] for data in serializer.data]

        return list(set(existing + new_keys))

    def create(self):
        serializer = KeywordSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer

    def create_multiple(self):
        self.validation_format_datas_in_data_multiple()

        list_data = self.serializer.data['datas']
        self.type = self.serializer.data['return_type']
        return_list = list()

        for data in list_data:
            self.data = data
            result = self.return_type(serializer=self.create())

            return_list.append(result)

        return return_list

    def update(self):
        serializer = KeywordSerializer(
            instance=self.instance,
            data=self.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer

    def update_or_create_multiple(self):
        self.type = 'id'
        return_list = list()

        if self.datas:
            for data in self.datas:
                if data.get('id', False):
                    queryset = Keyword.objects.filter(id=data['id'])

                    if queryset.exists():
                        serializer = KeywordSerializer(
                            instance=queryset.first(),
                            data=data,
                            partial=True
                        )
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
                    else:
                        self.data = data
                        serializer = self.create()
                else:
                    self.data = data
                    serializer = self.create()

                result = self.return_type(serializer=serializer)
                return_list.append(result)

        if return_list:
            return_list = self.concat_list_keywords_with_existing(
                new_keys=return_list
            )

        return return_list
