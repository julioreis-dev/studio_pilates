from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    """
    Classbasedview com a responsabilidade de renderizar a página index.html
    """
    template_name = 'home/home.html'
