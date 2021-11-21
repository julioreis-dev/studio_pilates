from django.contrib import admin
from alunos.models.models_alunos import People
from alunos.models.models_turmas import Turmas


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_insc', 'email', 'active')
    search_fields = ['name', 'tel1']


class TurmasAdmin(admin.ModelAdmin):
    list_display = ('day', 'schedule')
    search_fields = ['day', 'schedule']


admin.site.register(People, PeopleAdmin)
admin.site.register(Turmas, TurmasAdmin)
