from rest_framework import serializers
from articles.models import Article
from categories.serializers import CategoryDetailSerializer
from keywords.serializers import KeywordSerializer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleDetailSerializer(ArticleSerializer):
    category = CategoryDetailSerializer()
    keywords = KeywordSerializer(many=True, read_only=True)
