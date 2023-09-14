from django.db import models
from utilities.models import CreatedUpdatedAt
from django.contrib.auth.models import User


class Author(CreatedUpdatedAt):
    user = models.OneToOneField(
        to=User,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name='Usuário'
    )
    bibliography = models.TextField(
        blank=True,
        null=True,
        verbose_name='Bibliografia'
    )
    is_active = models.BooleanField(default=True,)

    def __str__(self) -> str:
        return f'{self.id} - {self.user.first_name} {self.user.last_login}'
