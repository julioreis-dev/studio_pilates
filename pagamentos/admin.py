from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import get_template
from django_object_actions import DjangoObjectActions
from pagamentos.models.models_pagamentos import Payments
from django.utils.timezone import now
from xhtml2pdf import pisa


class PaymentsAdmin(DjangoObjectActions, admin.ModelAdmin):
    """
    Class de contextualização do admin para o model Payments
    """
    list_display = ('boletim', 'invoice', 'month', 'year_db', 'pay')
    search_fields = ('boletim__people__name', 'boletim__ano', 'month', 'id', 'pay')
    # Contextualizando dados de dashboards
    Payments.year_db.short_description = 'Ano'
    Payments.invoice.short_description = 'Nº Recibo'

    def generate_pdf_payments(self, request, obj):
        """
        Method: Método responsável de gerar o PDF por meio do botão inserido no admin

        :param request: request
        :param obj: Fields do models Payments
        :return: erro ou response
        """
        template_path = 'reports/pdf_invoice.html'
        context = {'obj': obj, 'schedule': now}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{obj}.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response)
        return HttpResponse('We had some errors <pre>' + html + '</pre>') if pisa_status.err else response

    # Criando o botão no admin
    generate_pdf_payments.label = 'Gerar Recibo'
    generate_pdf_payments.short_description = 'Clique para gerar o recibo do aluno em PDF'

    # Registrando o método
    change_actions = ('generate_pdf_payments',)


admin.site.register(Payments, PaymentsAdmin)
