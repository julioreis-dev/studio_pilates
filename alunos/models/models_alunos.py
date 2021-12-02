from django.db import models
from django.utils.timezone import now
from alunos.models import DAY_CHOICE, SCHEDULE_CHOICE, STATUS_CHOICE


class People(models.Model):
    """
    Classe model para cadastro de pessoas usuárias da academia
    """
    name = models.CharField(max_length=200, verbose_name='nome')
    birthday = models.DateField(default=now, verbose_name='Nascimento', editable=True)
    date_insc = models.DateField(default=now, verbose_name='Data de inscrição', editable=True)
    profession = models.CharField(max_length=150, blank=True, verbose_name='Profissão')
    address = models.CharField(max_length=250, verbose_name='Endereço', null=True, blank=True)
    email = models.EmailField(max_length=200, verbose_name='Email', unique=True)
    tel1 = models.CharField(max_length=11, unique=True, verbose_name='Telefone (1)',
                            help_text="Telefone do aluno")
    tel2 = models.CharField(max_length=11, null=True, blank=True, unique=True, verbose_name='Telefone (2)',
                            help_text="Telefone de emergência")
    insta = models.CharField(max_length=150, blank=True, verbose_name='Instagram')
    day = models.CharField(choices=DAY_CHOICE, max_length=20, default='segunda-feira', verbose_name='Dia')
    schedule = models.CharField(choices=SCHEDULE_CHOICE, max_length=2, default='m1', verbose_name='Horário')
    status = models.CharField(choices=STATUS_CHOICE, default='ativo', max_length=7)

    def day_schedules(self):
        """
        Method: Metodo para verificar se o aluno esta alocado dentro da turma desejada ou não, alem de verificar se
        o mesmo esta alocado em mais de uma turma e se esta inativo. O metodo é apresentado na tela de admin
        relativo a aluno.

        :return: Situação do aluno
        """
        t = People.objects.filter(id=self.id)
        right_day = t[0].day
        right_sched = t[0].schedule
        z = t[0].turmas_set.all()
        if t[0].status == 'inativo':
            return 'Temporariamente inativo'
        else:
            if len(z) == 1 or len(z) == 0:
                if z.exists():
                    day_turma = z.values_list('day').first()
                    sched_turma = z.values_list('schedule').first()
                    if right_day == day_turma[0] and right_sched == sched_turma[0]:
                        return 'Alocado'
                    else:
                        return 'Alocado (fora do horário)'
                else:
                    return 'Aguardando alocação'
            else:
                return f'Alocado em {len(z)} horários'

    def __str__(self):
        """
        Retorna a associação do field nome para identificar a instacia

        :return: Identificação da instancia
        """
        return f'{self.name}'

    class Meta:
        """
        Classe para ordenar e contextualizar o admin
        """
        ordering = ('-date_insc',)
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
