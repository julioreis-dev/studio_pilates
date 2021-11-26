from django.db import models
from alunos.models.models_alunos import People

import datetime

year = datetime.date.today().year


class Bills(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE, verbose_name="Aluno")
    ano = models.IntegerField(verbose_name="Ano da turma", help_text=f'ex: {year}', default=year)

    def __str__(self):
        return f'{self.people}'

    class Meta:
        verbose_name = 'Boleto'
        verbose_name_plural = 'Boletos'
