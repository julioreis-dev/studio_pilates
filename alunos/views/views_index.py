from django.shortcuts import render
from django.views.generic import TemplateView

class IndexTemplateView(TemplateView):
    template_name = 'home/home.html'
    # template_name = 'inner-page.html'