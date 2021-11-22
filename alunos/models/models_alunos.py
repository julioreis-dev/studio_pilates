from django.db import models
from django.utils.timezone import now
from alunos.models import DAY_CHOICE, SCHEDULE_CHOICE, STATUS_CHOICE


class People(models.Model):
    name = models.CharField(max_length=200, verbose_name='nome')
    birthday = models.DateField(default=now, verbose_name='Nascimento', editable=True)
    date_insc = models.DateField(default=now, verbose_name='Data de inscrição', editable=True)
    profession = models.CharField(max_length=150, blank=True, verbose_name='Profissão')
    address = models.CharField(max_length=250, verbose_name='Endereço', null=True, blank=True)
    email = models.EmailField(max_length=200, verbose_name='Email')
    tel1 = models.CharField(max_length=11, unique=True, verbose_name='Telefone (1)',
                            help_text="Telefone do aluno")
    tel2 = models.CharField(max_length=11, null=True, blank=True, unique=True, verbose_name='Telefone (2)',
                            help_text="Telefone de emergência")
    insta = models.CharField(max_length=150, blank=True, verbose_name='Instagram')
    day = models.CharField(choices=DAY_CHOICE, max_length=20, default='segunda-feira', verbose_name='Dia')
    schedule = models.CharField(choices=SCHEDULE_CHOICE, max_length=2, default='m1', verbose_name='Horário')
    status = models.CharField(choices=STATUS_CHOICE, default='ativo', max_length=7)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('-date_insc',)
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
