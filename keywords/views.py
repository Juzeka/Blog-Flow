from rest_framework.viewsets import ModelViewSet
from keywords.serializers import Keyword, KeywordSerializer


class KeywordViewSet(ModelViewSet):
    serializer_class = KeywordSerializer
    queryset = Keyword.objects.filter(is_active=True)
