from rest_framework.viewsets import ModelViewSet
from comments.serializers import Comment, CommentSerializer
from utilities.choices import APPROVED_CHOICE


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(status=APPROVED_CHOICE)
