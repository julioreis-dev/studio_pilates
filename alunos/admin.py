from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import get_template
from django_object_actions import DjangoObjectActions
from alunos.models.models_boleto import Bills
from alunos.models.models_pagamentos import Payments
from alunos.models.models_alunos import People
from alunos.models.models_turmas import Turmas
from django.utils.timezone import now
from xhtml2pdf import pisa


class PaymentsInline(admin.TabularInline):
    """
    Class criada para integrar os dados de Payments com a class Bills
    """
    model = Payments
    extra = 0


class PeopleAdmin(admin.ModelAdmin):
    """
    Class de contextualização do admin para o model People
    """
    list_display = ('name', 'date_insc', 'email', 'day_schedules', 'status')
    search_fields = ['name', 'tel1', 'status']

    # Contextualizando dados de dashboards
    People.day_schedules.short_description = 'Status Alocação'


class TurmasAdmin(DjangoObjectActions, admin.ModelAdmin):
    """
    Class de contextualização do admin para o model Turmas
    """
    list_display = ('day', 'schedule', 'total')
    search_fields = ['day', 'schedule', 'alunos__name']
    filter_horizontal = ('alunos',)

    # Contextualizando dados de dashboards
    Turmas.total.short_description = 'Disponibilidade'

    def generate_pdf_class(self, request, obj):
        """
        Method: Método responsável de gerar o PDF por meio do botão inserido no admin

        :param request: request
        :param obj: Fields do models Turmas
        :return: erro ou response
        """
        infos = obj.alunos.all()
        template_path = 'reports/pdf_class.html'
        context = {'infos': infos, 'obj': obj, 'schedule': now}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{obj}.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response)
        return HttpResponse('We had some errors <pre>' + html + '</pre>') if pisa_status.err else response

    # Criando o botão no admin
    generate_pdf_class.label = 'Gerar Relatório'
    generate_pdf_class.short_description = 'Clique para gerar o PDF do relatório desse aluno'

    # Registrando o método
    change_actions = ('generate_pdf_class',)


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
    generate_pdf.short_description = 'Clique para gerar o PDF do relatório desse aluno'

    # Registrando o método
    change_actions = ('generate_pdf',)


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
    generate_pdf_payments.short_description = 'Clique para gerar o recibo em PDF do referido aluno'

    # Registrando o método
    change_actions = ('generate_pdf_payments',)


# Registro dos models e das classes de contextualização do admin
admin.site.register(People, PeopleAdmin)
admin.site.register(Turmas, TurmasAdmin)
admin.site.register(Bills, BillsAdmin)
admin.site.register(Payments, PaymentsAdmin)
