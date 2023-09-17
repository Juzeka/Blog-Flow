from django.db import models
from utilities.models import CreatedUpdatedAt
from utilities.choices import (
    STATUS_ARTICLE_CHOICES,
    WAITING_PUBLICATION_CHOICE
)


class Article(CreatedUpdatedAt):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    subtitle = models.CharField(max_length=250, verbose_name='SubTitulo')
    content = models.TextField(verbose_name='Conteúdo')
    status = models.CharField(
        max_length=50,
        choices=STATUS_ARTICLE_CHOICES,
        default=WAITING_PUBLICATION_CHOICE,
        verbose_name='Status'
    )
    author = models.ForeignKey(
        to='author.Author',
        on_delete=models.PROTECT,
        related_name='a_authors',
        verbose_name='Categoria'
    )
    category = models.ForeignKey(
        to='categories.Category',
        on_delete=models.DO_NOTHING,
        related_name='a_categories',
        verbose_name='Categoria'
    )
    keywords = models.ManyToManyField(
        to='keywords.Keyword',
        related_name='a_keywords',
        verbose_name='Palavras-chave'
    )
    is_visible = models.BooleanField(default=False, verbose_name='Visível')

    def __str__(self) -> str:
        return f'{self.id} - {self.title}'
