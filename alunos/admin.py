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
    model = Payments
    extra = 0


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_insc', 'email', 'day_schedules', 'status')
    search_fields = ['name', 'tel1', 'status']

    People.day_schedules.short_description = 'Status Alocação'


class TurmasAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('day', 'schedule', 'total')
    search_fields = ['day', 'schedule', 'alunos__name']
    filter_horizontal = ('alunos',)

    Turmas.total.short_description = 'Disponibilidade'

    def generate_pdf_class(self, request, obj):
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

    generate_pdf_class.label = 'Gerar Relatório'
    generate_pdf_class.short_description = 'Clique para gerar o PDF do relatório desse aluno'

    change_actions = ('generate_pdf_class',)


class BillsAdmin(DjangoObjectActions, admin.ModelAdmin):
    raw_id_fields = ('people',)
    list_display = ('people', 'ano')
    inlines = (PaymentsInline,)
    search_fields = ('people__name', 'ano')

    def generate_pdf(self, request, obj):
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

    generate_pdf.label = 'Gerar Relatório'
    generate_pdf.short_description = 'Clique para gerar o PDF do relatório desse aluno'

    change_actions = ('generate_pdf',)


class PaymentsAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('boletim', 'invoice', 'month', 'month_db', 'pay')
    search_fields = ('boletim__people__name', 'boletim__ano', 'month', 'id', 'pay')

    Payments.month_db.short_description = 'Ano'
    Payments.invoice.short_description = 'Nº Recibo'

    def generate_pdf_payments(self, request, obj):
        template_path = 'reports/pdf_invoice.html'
        context = {'obj': obj, 'schedule': now}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{obj}.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response)
        return HttpResponse('We had some errors <pre>' + html + '</pre>') if pisa_status.err else response

    generate_pdf_payments.label = 'Gerar Recibo'
    generate_pdf_payments.short_description = 'Clique para gerar o recibo em PDF do referido aluno'

    change_actions = ('generate_pdf_payments',)


admin.site.register(People, PeopleAdmin)
admin.site.register(Turmas, TurmasAdmin)
admin.site.register(Bills, BillsAdmin)
admin.site.register(Payments, PaymentsAdmin)
