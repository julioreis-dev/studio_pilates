import datetime
from django.db import models
from alunos.models import MONTH_CHOICE
from alunos.models.models_boleto import Bills



def default_month():
    months = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
              9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    name_month = datetime.date.today().month
    return months[name_month]


class Payments(models.Model):
    boletim = models.ForeignKey(Bills, blank=True, on_delete=models.CASCADE, null=True)
    val = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='valor', default=0.00)
    month = models.CharField(choices=MONTH_CHOICE, max_length=10, default=default_month(), verbose_name='Mês')
    pay = models.BooleanField(verbose_name='Pago', default=False)

    def month_db(self):
        x = Payments.objects.filter(id=self.id).first()
        return x.boletim.ano

    def invoice(self):
        return self.id

    def __str__(self):
        return f'{self.boletim}'

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
