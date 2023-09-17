from rest_framework import serializers
from keywords.models import Keyword


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class KeywordDetailArticleSerializer(KeywordSerializer):
    class Meta(KeywordSerializer.Meta):
        fields = ['id', 'name']


class NameChildSerializer(serializers.Serializer):
    name = serializers.CharField()


class KeywordMultipleSerializer(serializers.Serializer):
    datas = serializers.ListField(child=NameChildSerializer())
    return_type = serializers.ChoiceField(
        choices=['serializer', 'instance', 'data', 'id'],
        default='serializer'
    )
