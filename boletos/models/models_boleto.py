from django.db import models
from alunos.models.models_alunos import People
import datetime

year = datetime.date.today().year


class Bills(models.Model):
    """
    Classe model Bills para registro de boletos de pagamentos mensais realizados no corrente ano pelos
    usuários da academia
    """
    people = models.ForeignKey(People, on_delete=models.CASCADE, verbose_name="Aluno")
    ano = models.IntegerField(verbose_name="Ano da turma", help_text=f'ex: {year}', default=year)

    def __str__(self):
        """
        Retorna a associação do relacionamento People para identificar a instacia

        :return: Identificação da instancia
        """
        return f'{self.people}'

    class Meta:
        """
        Classe para ordenar e contextualizar o admin
        """
        verbose_name = 'Boleto'
        verbose_name_plural = 'Boletos'
        unique_together = ['people', 'ano']
