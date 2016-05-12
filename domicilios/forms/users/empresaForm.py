# -*- coding: utf-8 -*-

from django import forms
from PIL import Image
from django.forms import widgets
from domicilios.models.users import Empresa
from django.contrib.auth.hashers import make_password

class AddEmpresaForm(forms.ModelForm):
	class Meta:
		model = Empresa
		fields = ('nit', 'first_name', 'logo', 'web', 'username', 'ciudad', 'direccion')
		widgets = {
		"username": forms.TextInput(attrs={'placeholder':'Codigo Sede'}),
		"web": forms.TextInput(attrs={'placeholder':'http://www.ejemplo.co/'}),
		"nit": forms.TextInput(attrs={'placeholder':'Nit'}),
		"first_name": forms.TextInput(attrs={'placeholder':'Nombre de la Empresa'}),
		"logo": forms.FileInput(attrs={'placeholder':'Direccion', 'style':'display:none'}),
		"direccion": forms.TextInput(attrs={'placeholder':'Direccion'}),
		"ciudad": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
        }

class EditEmpresaForm(forms.ModelForm):
	class Meta:
		model = Empresa
		fields = ('nit', 'first_name', 'logo', 'web', 'username', 'ciudad', 'direccion')
		widgets = {
		"username": forms.TextInput(attrs={'placeholder':'UserName'}),
		"web": forms.TextInput(attrs={'placeholder':'http://www.ejemplo.co/'}),
		"nit": forms.TextInput(attrs={'placeholder':'Nit'}),
		"first_name": forms.TextInput(attrs={'placeholder':'Nombre de la Empresa'}),
		"logo": forms.FileInput(attrs={'placeholder':'Direccion', 'style':'display:none'}),
		"direccion": forms.TextInput(attrs={'placeholder':'Direccion'}),
		"ciudad": forms.Select(attrs={'class':'ui search dropdown'}),
        }


