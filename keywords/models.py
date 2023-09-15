from django.db import models
from utilities.models import CreatedUpdatedAt


class Keyword(CreatedUpdatedAt):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self) -> str:
        return self.name
