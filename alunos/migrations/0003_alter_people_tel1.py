# Generated by Django 3.2.9 on 2021-11-18 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_auto_20211117_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='tel1',
            field=models.IntegerField(blank=True, help_text='Telefone do aluno', null=True, unique=True, verbose_name='Telefone (1)'),
        ),
    ]
