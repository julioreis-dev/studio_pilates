from django.db import models
from alunos.models import MONTH_CHOICE
from alunos.models.models_boleto import Bills


class Payments(models.Model):
    boletim = models.ForeignKey(Bills, blank=True, on_delete=models.CASCADE, null=True)
    val = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='valor')
    month = models.CharField(choices=MONTH_CHOICE, max_length=10, default='janeiro', verbose_name='Mês')
    pay = models.BooleanField(verbose_name='Pago', default=False)

    def __str__(self):
        return f'{self.boletim}'

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
