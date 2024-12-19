from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from .models import Feedback
# from .services import get_info


# Create your views here.


class WebLending(TemplateView):
    template_name = 'web/index.html'


class WebMobile(TemplateView):
    template_name = 'web/mobileweb.html'

# def add_feed(request):
#     email = request.POST('email')
#     Feedback.objects.create(email=email)
#     return redirect('/mobile')


class FeedbackOrder(CreateView):
    fields = ('email',)
    model = Feedback
    success_url = '/mobile'


# class
# class LoginView(TemplateView):
#     template_name = 'web/login.html'





# расспредилить всё логику