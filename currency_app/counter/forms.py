from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='username', widget=forms.TextInput)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User

class LoginForm(forms.Form):
    username_ = forms.CharField(label='username_', widget=forms.TextInput)
    password_ = forms.CharField(label='password_', widget=forms.PasswordInput)

    class Meta:
        model = User


