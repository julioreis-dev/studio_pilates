# Generated by Django 3.2.9 on 2021-11-18 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0005_alter_people_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'Aluno', 'verbose_name_plural': 'Alunos'},
        ),
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='people',
            name='insta',
            field=models.CharField(blank=True, max_length=150, verbose_name='Instagram'),
        ),
    ]
