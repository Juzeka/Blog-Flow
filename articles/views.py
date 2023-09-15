from rest_framework.viewsets import ModelViewSet
from articles.serializers import Article, ArticleSerializer
from utilities.choices import PUBLISHED_CHOICE


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(status=PUBLISHED_CHOICE, is_visible=True)
