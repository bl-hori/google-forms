from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView

from base.forms import *


def home(request):
    template = loader.get_template("base/home.html")
    ctx = {"title": "Django Home"}
    return HttpResponse(template.render(ctx, request))


class LoginView(LoginView):
    template_name = 'base/login.html'
    form_class = LoginForm

class LogoutView(LogoutView):
    template_name = 'base/logout.html'


class SignupView(CreateView):
    template_name = 'base/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('home')
