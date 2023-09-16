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
