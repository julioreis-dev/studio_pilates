from django.urls import path
from alunos.views.views_index import IndexTemplateView


app_name = 'index'

urlpatterns = [path('', IndexTemplateView.as_view(), name='index'),]