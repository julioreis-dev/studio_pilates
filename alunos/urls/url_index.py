from django.urls import path
from alunos.views.views_index import IndexTemplateView


# URL que acessa o template index.html por meio da classbasedview IndexTemplateView

app_name = 'index'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    ]
