from django.contrib import admin
from alunos.models.models_alunos import People
from alunos.models.models_turmas import Turmas


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_insc', 'email', 'active')
    search_fields = ['name', 'tel1', 'active']


class TurmasAdmin(admin.ModelAdmin):
    list_display = ('day', 'schedule')
    search_fields = ['day', 'schedule']
    filter_horizontal = ('alunos',)


admin.site.register(People, PeopleAdmin)
admin.site.register(Turmas, TurmasAdmin)
