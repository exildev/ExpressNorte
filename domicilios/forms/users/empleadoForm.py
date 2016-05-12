# -*- coding: utf-8 -*-

from django import forms
from django.forms import widgets
from domicilios.models.users import Empleado
from django.contrib.auth.hashers import make_password

class AddEmpleadoForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = ('username','first_name', 'last_name', 'tipo_id', 'identificacion', 'cargo', 'fecha_nacimiento', 'empresa' ,'password','telefono_fijo', 'telefono_celular', 'email', 'direccion', 'ciudad')
		widgets = {
		"username": forms.TextInput(attrs={'placeholder':'Nombre de Usuario'}),
		"first_name": forms.TextInput(attrs={'placeholder':'Nombres', 'required':True}),
		"last_name": forms.TextInput(attrs={'placeholder':'Apellidos', 'required':True}),
		"identificacion": forms.TextInput(attrs={'placeholder':'Numero de Identificación'}),
		"telefono_fijo": forms.TextInput(attrs={'placeholder':'Telefono Fijo'}),
		"telefono_celular": forms.TextInput(attrs={'placeholder':'Telefono Celular'}),
		"direccion": forms.TextInput(attrs={'placeholder':'Direccion'}),
		"ciudad": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		"tipo_id": forms.Select(attrs={'class':'ui dropdown'}),
		"cargo": forms.Select(attrs={'class':'ui dropdown'}),
        "fecha_nacimiento":forms.DateInput(attrs={'placeholder': 'Ingrese Fecha de Nacimiento 31/12/2015', 'type':'date'}),
        "empresa": forms.Select(attrs={'class':'ui search dropdown'}),
        "password": forms.PasswordInput(attrs={'placeholder': 'Ingrese Contraseña'}),
		"email": forms.EmailInput(attrs={'Placeholder':'Email', 'required':True}),
        }

	def save(self, commit=True):
		self.instance.password = make_password(self.instance.password)
		return super(AddEmpleadoForm, self).save(commit)

class AddEmpleadoApiForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = ('username','first_name', 'last_name', 'tipo_id', 'identificacion', 'cargo', 'fecha_nacimiento', 'empresa' ,'password','telefono_fijo', 'telefono_celular', 'email', 'direccion', 'ciudad')
		exclude = ('empresa',)
		widgets = {
		"username": forms.TextInput(attrs={'placeholder':'Nombre de Usuario'}),
		"first_name": forms.TextInput(attrs={'placeholder':'Nombres', 'required':True}),
		"last_name": forms.TextInput(attrs={'placeholder':'Apellidos', 'required':True}),
		"identificacion": forms.TextInput(attrs={'placeholder':'Numero de Identificación'}),
		"telefono_fijo": forms.TextInput(attrs={'placeholder':'Telefono Fijo'}),
		"telefono_celular": forms.TextInput(attrs={'placeholder':'Telefono Celular'}),
		"direccion": forms.TextInput(attrs={'placeholder':'Direccion'}),
		"ciudad": forms.Select(attrs={'class':'ui search dropdown'}),
		"tipo_id": forms.Select(attrs={'class':'ui dropdown'}),
		"cargo": forms.Select(attrs={'class':'ui dropdown'}),
        "fecha_nacimiento": forms.DateInput(attrs={'placeholder': 'Ingrese Fecha de Nacimiento 31/12/2015', 'type':'date'}),
        "password": forms.PasswordInput(attrs={'placeholder': 'Ingrese Contraseña'}),
		"email": forms.EmailInput(attrs={'Placeholder':'Email', 'required':True}),
        }

	def save(self, commit=True):
		self.instance.password = make_password(self.instance.password)
		return super(AddEmpleadoApiForm, self).save(commit)

class EditEmpleadoForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = ('username','first_name', 'last_name', 'tipo_id', 'identificacion', 'cargo', 'fecha_nacimiento', 'empresa' ,'telefono_fijo', 'telefono_celular', 'email', 'direccion', 'ciudad')
		widgets = {
		"username": forms.TextInput(attrs={'placeholder':'Nombre de Usuario'}),
		"first_name": forms.TextInput(attrs={'placeholder':'Nombres', 'required':True}),
		"last_name": forms.TextInput(attrs={'placeholder':'Apellidos', 'required':True}),
		"identificacion": forms.TextInput(attrs={'placeholder':'Numero de Identificación'}),
		"telefono_fijo": forms.TextInput(attrs={'placeholder':'Telefono Fijo'}),
		"telefono_celular": forms.TextInput(attrs={'placeholder':'Telefono Celular'}),
		"direccion": forms.TextInput(attrs={'placeholder':'Direccion'}),
		"ciudad": forms.Select(attrs={'class':'ui search dropdown'}),
		"tipo_id": forms.Select(attrs={'class':'ui dropdown'}),
		"cargo": forms.Select(attrs={'class':'ui dropdown'}),
        "fecha_nacimiento": forms.DateInput(attrs={'placeholder': 'Ingrese Fecha de Nacimiento 31/12/2015', 'type':'date'}),
        "empresa": forms.Select(attrs={'class':'ui dropdown'}),
		"email": forms.EmailInput(attrs={'Placeholder':'Email', 'required':True}),
        }

class EditEmpleadoApiForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = ('username','first_name', 'last_name', 'tipo_id', 'identificacion', 'cargo', 'fecha_nacimiento', 'empresa' ,'telefono_fijo', 'telefono_celular', 'email', 'direccion', 'ciudad')
		exclude = ('empresa',)
		widgets = {
		"username": forms.TextInput(attrs={'placeholder':'Nombre de Usuario'}),
		"first_name": forms.TextInput(attrs={'placeholder':'Nombres', 'required':True}),
		"last_name": forms.TextInput(attrs={'placeholder':'Apellidos', 'required':True}),
		"identificacion": forms.TextInput(attrs={'placeholder':'Numero de Identificación'}),
		"telefono_fijo": forms.TextInput(attrs={'placeholder':'Telefono Fijo'}),
		"telefono_celular": forms.TextInput(attrs={'placeholder':'Telefono Celular'}),
		"direccion": forms.TextInput(attrs={'placeholder':'Direccion'}),
		"ciudad": forms.Select(attrs={'class':'ui search dropdown'}),
		"tipo_id": forms.Select(attrs={'class':'ui dropdown'}),
		"cargo": forms.Select(attrs={'class':'ui dropdown'}),
        "fecha_nacimiento": forms.DateInput(attrs={'placeholder': 'Ingrese Fecha de Nacimiento 31/12/2015', 'type':'date'}),
		"email": forms.EmailInput(attrs={'Placeholder':'Email', 'required':True}),
        }

class PassChangeEmpleadoForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = ('password',)
		widgets = {
        "password": forms.PasswordInput(attrs={'placeholder': 'Ingrese Nueva Contraseña'}),
        }

	def save(self, commit=True):
		self.instance.password = make_password(self.instance.password)
		return super(PassChangeEmpleadoForm, self).save(commit)
