from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import get_template
from django_object_actions import DjangoObjectActions
from turmas.models.models_turmas import Turmas
from django.utils.timezone import now
from xhtml2pdf import pisa


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

        :return: erro ou a criação do conteúdo em PDF
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
    generate_pdf_class.label = 'Lista de Alunos'
    generate_pdf_class.short_description = 'Clique para gerar a lista de alunos da turma em PDF'

    # Registrando o método
    change_actions = ('generate_pdf_class',)


admin.site.register(Turmas, TurmasAdmin)
