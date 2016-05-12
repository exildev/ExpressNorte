# -*- coding: utf-8 -*-
from django import forms
from domicilios.models.pedido import *
from domicilios.models.users import Empleado

class AddPedidoForm(forms.ModelForm):
	alistador = forms.ModelChoiceField(queryset=Empleado.objects.filter(cargo='ALISTADOR'), widget=forms.Select(attrs={'class':'ui fluid search selection dropdown', 'placeholder':'Alistador'}))
	supervisor = forms.ModelChoiceField(queryset=Empleado.objects.filter(cargo='SUPERVISOR'), widget=forms.Select(attrs={'class':'ui fluid search selection dropdown', 'placeholder':'Supervisor'}))
	class Meta:
		model = Pedido
		fields = '__all__'
		exclude = ('motorizado','total', 'npedido_express','entregado','despachado','confirmado','alistado',)
		widgets = {
		"cliente": forms.Select(attrs={'class':'ui fluid search selection dropdown','placeholder':'Cliente'}),
		"tipo_pago": forms.Select(attrs={'class':'ui dropdown', 'placeholder':'Tipo de Pago'}),
		"empresa": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		"tienda": forms.TextInput(attrs={'placeholder':'Tienda'}),
		"num_pedido": forms.TextInput(attrs={'placeholder':'Numero de Pedido'}),
		"observacion": forms.Textarea(attrs={'rows':'4','placeholder':'Observaciones'}),
        }

#Clase para el formulario de pedidos del administrador
class AddPedidoAdminForm(forms.ModelForm):
	alistador = forms.ModelChoiceField(queryset=Empleado.objects.filter(cargo='ALISTADOR'), widget=forms.Select(attrs={'class':'ui fluid search selection dropdown', 'placeholder':'Alistador'}))
	supervisor = forms.ModelChoiceField(queryset=Empleado.objects.filter(cargo='SUPERVISOR'), widget=forms.Select(attrs={'class':'ui fluid search selection dropdown', 'placeholder':'Supervisor'}))
	motorizado = forms.ModelChoiceField(queryset=Empleado.objects.filter(cargo='MOTORIZADO'), widget=forms.Select(attrs={'class':'ui fluid search selection dropdown', 'placeholder':'Motorizado'}))
	class Meta:
		model = Pedido
		fields = '__all__'
		exclude = ('total', 'npedido_express',)
		widgets = {
		"cliente": forms.Select(attrs={'class':'ui fluid search selection dropdown', 'placeholder':'Cliente'}),
		"tipo_pago": forms.Select(attrs={'class':'ui dropdown', 'placeholder':'Tipo de Pago'}),
		"empresa": forms.Select(attrs={'class':'ui fluid search selection dropdown', 'placeholder':'Empresa'}),
		"tienda": forms.TextInput(attrs={'placeholder':'Tienda'}),
		"num_pedido": forms.TextInput(attrs={'placeholder':'Numero de Pedido'}),
		"observacion": forms.Textarea(attrs={'rows':'4','placeholder':'Observaciones'}),
        }

class AddPedidoApiForm(forms.ModelForm):
	class Meta:
		model = Pedido
		fields = '__all__'
		exclude = ('motorizado','total','supervisor','empresa', 'npedido_express',)
		widgets = {
		"num_pedido": forms.TextInput(attrs={'placeholder':'Numero de Pedido'}),
		"tienda": forms.TextInput(attrs={'placeholder':'Tienda'}),
		"cliente": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		"alistador": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		"tipo_pago": forms.Select(attrs={'class':'ui dropdown'}),
		"observacion": forms.Textarea(attrs={'rows':'4','placeholder':'Observaciones'}),
        }

#Clase para el formulario de pedidos del administrador api

class AddPedidoAdminApiForm(forms.ModelForm):
	class Meta:
		model = Pedido
		fields = '__all__'
		exclude = ('total','empresa', 'npedido_express','motorizado',)
		widgets = {
		"num_pedido": forms.TextInput(attrs={'placeholder':'Numero de Pedido'}),
		"tienda": forms.TextInput(attrs={'placeholder':'Tienda'}),
		"cliente": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		"tipo_pago": forms.Select(attrs={'class':'ui dropdown'}),
		"observacion": forms.Textarea(attrs={'rows':'4','placeholder':'Observaciones'}),
		"alistador": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		"supervisor": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
        }

class EditPedidoAdminApiForm(forms.ModelForm):
	class Meta:
		model = Pedido
		fields = '__all__'
		exclude = ('total','empresa', 'npedido_express',)
		widgets = {
		"num_pedido": forms.TextInput(attrs={'placeholder':'Numero de Pedido'}),
		"tienda": forms.TextInput(attrs={'placeholder':'Tienda'}),
		"cliente": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		"tipo_pago": forms.Select(attrs={'class':'ui dropdown'}),
		"observacion": forms.Textarea(attrs={'rows':'4','placeholder':'Observaciones'}),
		"alistador": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		"supervisor": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		"motorizado": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
        }




class AddItemsForm(forms.ModelForm):
	class Meta:
		model = Items
		fields = '__all__'
		widgets = {
		"codigo": forms.TextInput(attrs={'placeholder':'Codigo'}),
		"descripcion": forms.Textarea(attrs={'rows':'2', 'placeholder':'Descripción'}),
		"presentacion": forms.Select(attrs={'class':'ui fluid search selection dropdown', 'placeholder':'Presentacion'}),
		"empresaI": forms.Select(attrs={'class':'ui fluid search selection dropdown', 'placeholder':'Empresa'}),
		}

class AddItemsApiForm(forms.ModelForm):
	class Meta:
		model = Items
		fields = '__all__'
		exclude = ('empresaI',)
		widgets = {
		"codigo": forms.TextInput(attrs={'placeholder':'Codigo'}),
		"descripcion": forms.Textarea(attrs={'rows':'2', 'placeholder':'Descripción'}),
		"presentacion": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		}

class AddItemsPedidoForm(forms.ModelForm):
	class Meta:
		model = ItemsPedido
		fields = '__all__'
		exclude = ('pedido','valor_total',)
		widgets = {
		"cantidad": forms.NumberInput(attrs={'placeholder':'Cantidad', 'step':'1'}),
		"valor_unitario": forms.NumberInput(attrs={'placeholder':'Valor Unitario'}),
		"item": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		}

class AddTiempoForm(forms.ModelForm):
	class Meta:
		model = Tiempo
		fields = '__all__'

class CertificadoForm(forms.ModelForm):
	class Meta:
		model = Certificado
		fields = '__all__'
		exclude = ('clienteC',)
		widgets = {
		"pedidoC": forms.Select(attrs={'class':'ui fluid search selection dropdown'}),
		"cedulaC": forms.FileInput(attrs={'style':'display:none'}),

		}
