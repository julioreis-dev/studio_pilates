# Generated by Django 3.2.9 on 2021-11-18 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0003_alter_people_tel1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nome'),
        ),
    ]
