import datetime
from django.db import models
from alunos.models import MONTH_CHOICE
from boletos.models.models_boleto import Bills



def default_month():
    """
    Função que retorna em portugês o nome do mês corrente

    :return: Nome do mês
    """
    months = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
              9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    name_month = datetime.date.today().month
    return months[name_month]


class Payments(models.Model):
    """
    Classe model Payments para cadastro de pagamentos mensais realizados
    """
    boletim = models.ForeignKey(Bills, blank=True, on_delete=models.CASCADE, null=True)
    val = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='valor', default=0.00)
    month = models.CharField(choices=MONTH_CHOICE, max_length=10, default=default_month(), verbose_name='Mês')
    pay = models.BooleanField(verbose_name='Pago', default=False)

    def year_db(self):
        """
        method: Metodo para retornar o ano do boletim e renderizar na tela de admin

        :return: Ano do pagamento
        """
        x = Payments.objects.filter(id=self.id).first()
        return x.boletim.ano

    def invoice(self):
        """
        method: Metodo para retornar o id do pagamento que será usado como numero da nota de pagamento. Este metodo
        é renderizado na tela de admin

        :return: Numero de id
        """
        return self.id

    def __str__(self):
        """
        Retorna a associação do field boletim para identificar a instacia

        :return: Identificação da instancia
        """
        return f'{self.boletim}'

    class Meta:
        """
        Classe para ordenar e contextualizar o admin
        """
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
