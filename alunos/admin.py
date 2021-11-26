from django.contrib import admin

from alunos.models import Bills
from alunos.models.models_pagamentos import Payments
from alunos.models.models_alunos import People
from alunos.models.models_turmas import Turmas


class PaymentsInline(admin.TabularInline):
    model = Payments
    extra = 0

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_insc', 'email', 'day_schedules', 'status')
    search_fields = ['name', 'tel1', 'status']

    People.day_schedules.short_description = 'Status Alocação'


class TurmasAdmin(admin.ModelAdmin):
    list_display = ('day', 'schedule', 'total')
    search_fields = ['day', 'schedule', 'alunos__name']
    filter_horizontal = ('alunos',)

    Turmas.total.short_description = 'Disponibilidade'


class BillsAdmin(admin.ModelAdmin):
    raw_id_fields = ('people',)
    list_display = ('people', 'ano')
    inlines = (PaymentsInline,)



admin.site.register(People, PeopleAdmin)
admin.site.register(Turmas, TurmasAdmin)
admin.site.register(Bills, BillsAdmin)
