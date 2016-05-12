# -*- coding: utf-8 -*-

from django import forms
from domicilios.models.users import Cliente

class AddClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ('first_name', 'last_name', 'tipo_id', 'identificacion','telefono_fijo', 'telefono_celular', 'direccion', 'barrio', 'zona', 'ciudad')
		widgets = {
			"first_name": forms.TextInput(attrs={'placeholder':'Nombres'}),
			"last_name": forms.TextInput(attrs={'placeholder':'Apellidos'}),
			"identificacion": forms.TextInput(attrs={'placeholder':'Numero de Identificación'}),
			"telefono_fijo": forms.TextInput(attrs={'placeholder':'Telefono Fijo'}),
			"telefono_celular": forms.TextInput(attrs={'placeholder':'Telefono Celular'}),
			"direccion": forms.TextInput(attrs={'placeholder':'Direccion'}),
			"ciudad": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
			"zona": forms.TextInput(attrs={'placeholder':'Zona'}),
			"barrio": forms.TextInput(attrs={'placeholder':'Barrio'}),
			"tipo_id": forms.Select(attrs={'class':'ui dropdown'}),
        }
