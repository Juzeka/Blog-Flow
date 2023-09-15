from django.db import models
from utilities.models import CreatedUpdatedAt
from utilities.choices import STATUS_COMMENTS_CHOICES, WAITING_APPROVED_CHOICE


class Comment(CreatedUpdatedAt):
    article = models.ForeignKey(
        to='articles.Article',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Artigo'
    )
    content = models.TextField(verbose_name='Comentário')
    status = models.CharField(
        max_length=50,
        choices=STATUS_COMMENTS_CHOICES,
        default=WAITING_APPROVED_CHOICE,
        verbose_name='Status'
    )

    def __str__(self) -> str:
        return f'{self.id} - {self.article.title}'
