# Generated by Django 3.2.9 on 2021-11-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0017_alter_people_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turmas',
            name='day',
            field=models.CharField(choices=[('segunda-feira', 'Segunda-Feira'), ('terça-feira', 'Terça-Feira'), ('quarta-feira', 'Quarta-Feira'), ('quinta-feira', 'Quinta-Feira'), ('sexta-feira', 'Sexta-Feira')], default=2, max_length=20, verbose_name='Dia'),
        ),
    ]
