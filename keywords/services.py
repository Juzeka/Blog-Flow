from keywords.serializers import KeywordSerializer


class KeywordServices:
    def __init__(self, *args, **kwargs) -> None:
        self.data_multiple = kwargs.get('data_multiple')
        self.data = kwargs.get('data')

    def create(self):
        serializer = KeywordSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer

    def create_multiple(self):
        list_data = self.data_multiple['datas']
        return_type = self.data_multiple['return_type']
        return_list = list()

        for data in list_data:
            self.data = data
            result = self.create()

            if return_type == 'instance':
                result = result.instance
            elif return_type == 'data':
                result = result.data

            return_list.append(result)

        return return_list
