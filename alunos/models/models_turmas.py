from django.db import models
from alunos.models import DAY_CHOICE, SCHEDULE_CHOICE


class Turmas(models.Model):
    day = models.CharField(choices=DAY_CHOICE, max_length=20, default='segunda-feira', verbose_name='Dia')
    schedule = models.CharField(choices=SCHEDULE_CHOICE, max_length=2, default='m1', verbose_name='Horário')

    def __str__(self):
        return f'{self.day} / {self.schedule}'

    class Meta:
        ordering = ('day',)
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
