# Generated by Django 4.2.3 on 2023-09-15 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Data de atualização')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Data de criação')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]