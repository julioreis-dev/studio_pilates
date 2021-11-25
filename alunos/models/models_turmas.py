from django.db import models
from alunos.models import DAY_CHOICE, SCHEDULE_CHOICE, People


class Turmas(models.Model):
    day = models.CharField(choices=DAY_CHOICE, max_length=20, default='segunda-feira', verbose_name='Dia')
    schedule = models.CharField(choices=SCHEDULE_CHOICE, max_length=2, default='m1', verbose_name='Horário')
    alunos = models.ManyToManyField(People, blank=True, help_text='Escolha os alunos da turma e transfira para a '
                                                                  'tabela da direita.')

    def total(self):
        number_student = self.alunos.count()
        disp = 3 - number_student
        if 0 < disp <= 3:
            return f'Disponível {disp} vaga(s)'
        elif disp < 0:
            return f'Turma com excedente de {abs(disp)} aluno(s)'
        else:
            return 'Turma completa'

    def __str__(self):
        return f'{self.day} / {self.schedule}'

    class Meta:
        ordering = ('day',)
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
