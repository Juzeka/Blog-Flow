from django.db import models


class CreatedUpdatedAt(models.Model):
    class Meta:
        abstract = True
        ordering = ['-created_at']

    created_at = models.DateTimeField(
        auto_now_add=True,
        auto_created=True,
        verbose_name='Data de criação'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        auto_created=True,
        verbose_name='Data de atualização'
    )
