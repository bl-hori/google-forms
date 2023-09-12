from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from base.models import User


class SignupForm(UserCreationForm):
    username = forms.CharField(label='メールアドレス')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='メールアドレス')
