# Generated by Django 3.2.9 on 2021-12-04 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0031_auto_20211203_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turmas',
            name='alunos',
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
        migrations.DeleteModel(
            name='Turmas',
        ),
    ]
