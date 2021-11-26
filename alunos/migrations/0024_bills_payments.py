# Generated by Django 3.2.9 on 2021-11-26 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0023_auto_20211121_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=2021, help_text='ex: 2021', verbose_name='Ano da turma')),
                ('people', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alunos.people')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor')),
                ('month', models.CharField(choices=[('janeiro', 'Janeiro'), ('fevereiro', 'Fevereiro'), ('março', 'Março'), ('abril', 'Abril'), ('maio', 'Maio'), ('junho', 'Junho'), ('julho', 'Julho'), ('agosto', 'Agosto'), ('setembro', 'Setembro'), ('outubro', 'Outubro'), ('novembro', 'Novembro'), ('dezembro', 'Dezembro')], default='janeiro', max_length=10, verbose_name='Mês')),
                ('pay', models.BooleanField(default=False, verbose_name='Pago')),
                ('boletim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alunos.bills')),
            ],
        ),
    ]
