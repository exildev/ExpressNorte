# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tu usuario', 'autofocus':True}), max_length=254)

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Tu contraseña'}))
