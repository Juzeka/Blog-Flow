# Generated by Django 4.2.3 on 2023-09-15 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Data de atualização')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Data de criação')),
                ('content', models.TextField(verbose_name='Comentário')),
                ('status', models.CharField(choices=[('waiting_approved', 'Aguardando aprovação'), ('approved', 'Aprovado'), ('disapproved', 'Reprovado')], default='waiting_approved', max_length=50, verbose_name='Status')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.article', verbose_name='Artigo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]