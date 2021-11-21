# Generated by Django 3.2.9 on 2021-11-18 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0010_auto_20211117_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='day',
            field=models.IntegerField(choices=[(2, 'Segunda-Feira'), (3, 'Terça-Feira'), (4, 'Quarta-Feira'), (5, 'Quinta-Feira'), (6, 'Sexta-Feira')], default=2, verbose_name='Dia'),
        ),
        migrations.AlterField(
            model_name='people',
            name='schedule',
            field=models.IntegerField(choices=[('Manhã', ((1, '07:00 / 08:00'), (2, '08:00 / 09:00'), (3, '09:00 / 10:00'), (4, '10:00 / 11:00'), (5, '11:00 / 12:00'))), ('Tarde/Noite', ((6, '16:00 / 17:00'), (7, '17:00 / 18:00'), (8, '18:00 / 19:00'), (9, '19:00 / 20:00'), (10, '20:00 / 21:00'), (11, '21:00 / 22:00')))], default=1, verbose_name='Horário'),
        ),
    ]
