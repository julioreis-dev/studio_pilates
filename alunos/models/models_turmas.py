from django.db import models
from alunos.models import DAY_CHOICE, SCHEDULE_CHOICE, People


class Turmas(models.Model):
    day = models.CharField(choices=DAY_CHOICE, max_length=20, default='segunda-feira', verbose_name='Dia')
    schedule = models.CharField(choices=SCHEDULE_CHOICE, max_length=2, default='m1', verbose_name='Horário')
    alunos = models.ManyToManyField(People, blank=True, help_text='Escolha os alunos da turma e transfira para a '
                                                                  'tabela da direita.')

    def total(self):
        tot = self.alunos.count()
        disp = 3-tot
        if disp == 1:
            return f'Disponível {disp} vaga.'
        elif disp > 1 and disp <= 3:
            return f'Disponível {disp} vagas.'
        elif disp < 0:
            return 'Turma com excedente'
        else:
            return 'Turma completa'


        # return f'Disponível {3-tot} vaga(s).' if tot < 3 else 'Turma completa'


    def __str__(self):
        return f'{self.day} / {self.schedule}'

    class Meta:
        ordering = ('day',)
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
