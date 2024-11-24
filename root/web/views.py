from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class WebLending(TemplateView):
    template_name = 'web/index.html'