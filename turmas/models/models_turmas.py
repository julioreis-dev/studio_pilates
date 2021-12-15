from django.db import models
from alunos.models import DAY_CHOICE, SCHEDULE_CHOICE, People


class Turmas(models.Model):
    """
    Classe model para Turmas que serão criadas pelo usuário
    """
    day = models.CharField(choices=DAY_CHOICE, max_length=20, default='segunda-feira', verbose_name='Dia')
    schedule = models.CharField(choices=SCHEDULE_CHOICE, max_length=2, default='m1', verbose_name='Horário')
    alunos = models.ManyToManyField(People, blank=True, help_text='Escolha os alunos da turma e transfira para a '
                                                                  'tabela da direita.')

    def total(self):
        """
        Method: Metodo para verificar a lotação permitida por aula. Total máximo permitido é 3 alunos por aula.

        :return: Numero de vagas disponível
        """
        number_student = self.alunos.count()
        disp = 3 - number_student
        if 0 < disp <= 3:
            return f'Disponível {disp} vaga(s)'
        elif disp < 0:
            return f'Turma com excedente de {abs(disp)} aluno(s)'
        else:
            return 'Turma completa'

    def __str__(self):
        """
        Retorna a associação entre os fields (day e schedule) para identificar a instacia

        :return: Identificação da instancia
        """
        return f'{self.day} / {self.schedule}'

    class Meta:
        """
        Classe para ordenar e contextualizar o admin
        """
        ordering = ('day',)
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        unique_together = ['day', 'schedule']
