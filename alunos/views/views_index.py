from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    """
    Class Based View que renderiza a página index.html
    """
    template_name = 'home/home.html'
