from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'
