from django.contrib import admin
from alunos.models.models_alunos import People


class PeopleAdmin(admin.ModelAdmin):
    """
    Class de contextualização do admin para o model People
    """
    fieldsets = (
        ('Dados Pessoais', {'fields': ('name', 'birthday','date_insc', 'profession', 'address', 'email', 'tel1',
                                       'tel2', 'insta')}),
        ('Horário Desejado', {'fields': ('day', 'schedule', 'status')}),
    )
    list_display = ('name', 'date_insc', 'email', 'day_schedules', 'status')
    search_fields = ('name', 'tel1', 'status')

    # Contextualizando dados de dashboards
    People.day_schedules.short_description = 'Status Alocação'


# Registro dos models e das classes de contextualização do admin
admin.site.register(People, PeopleAdmin)
