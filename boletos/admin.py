from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import get_template
from django_object_actions import DjangoObjectActions
from django.utils.timezone import now
from xhtml2pdf import pisa
from pagamentos.models.models_pagamentos import Payments
from boletos.models.models_boleto import Bills


class PaymentsInline(admin.TabularInline):
    """
    Class criada para integrar os dados de Payments com a class Bills
    """
    model = Payments
    extra = 0


class BillsAdmin(DjangoObjectActions, admin.ModelAdmin):
    """
    Class de contextualização do admin para o model Bills
    """
    raw_id_fields = ('people',)
    list_display = ('people', 'ano')
    inlines = (PaymentsInline,)
    search_fields = ('people__name', 'ano')

    def generate_pdf(self, request, obj):
        """
        Method: Método responsável de gerar o PDF por meio do botão inserido no admin

        :param request: request
        :param obj: Fields do models Bills
        :return: erro ou response
        """
        infos = obj.payments_set.all()
        template_path = 'reports/pdf_template.html'
        context = {'infos': infos, 'obj': obj, 'schedule': now}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{obj}.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response)

        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

    # Criando o botão no admin
    generate_pdf.label = 'Gerar Relatório'
    generate_pdf.short_description = 'Clique para gerar o relatório do aluno em PDF'

    # Registrando o método
    change_actions = ('generate_pdf',)


admin.site.register(Bills, BillsAdmin)
