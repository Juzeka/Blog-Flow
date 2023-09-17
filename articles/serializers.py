from rest_framework import serializers
from articles.models import Article
from categories.serializers import CategoryDetailSerializer
from keywords.serializers import KeywordSerializer
from comments.serializers import CommentDetailSerializer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleDetailSerializer(ArticleSerializer):
    category = CategoryDetailSerializer(read_only=True)
    keywords = KeywordSerializer(many=True, read_only=True)


class ArticleDetailFullSerializer(ArticleSerializer):
    comments = CommentDetailSerializer(many=True, read_only=True)

    class Meta(ArticleDetailSerializer.Meta):
        fields = [
            'id', 'title', 'subtitle', 'content', 'status', 'author',
            'category', 'keywords', 'is_visible', 'comments'
        ]
