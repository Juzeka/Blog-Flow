# Generated by Django 4.2.3 on 2023-09-17 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_keywords_article_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_visible',
            field=models.BooleanField(default=False, verbose_name='Visível'),
        ),
    ]
