# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from domicilios.forms.users.clienteForm import AddClienteForm
from domicilios.models.users import Cliente
from django.db.models import Q
from domicilios.decorators import *

@supervisor_required
def addCliente(request):
	if request.method == 'POST':
		form = AddClienteForm(request.POST)
		if form.is_valid():
			form.save()
			mensaje = {'tipo':'success','texto':'Se a registrado un cliente correctamente'}
			form =AddClienteForm()
			return render(request,'users/Cliente/index.html',{'mensaje':mensaje})
	else:
		form = AddClienteForm()
	return render(request,'users/Cliente/addCliente.html',{'form':form})

@administrador_required
def editCliente(request,cliente_id):
	cliente = Cliente.objects.get(id = cliente_id)

	if request.method == 'POST':
		form = AddClienteForm(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
			mensaje = {'tipo':'success','texto':"Se a editado un cliente correctamente"}
			form = AddClienteForm(instance=cliente)
			return render(request,'users/Cliente/editCliente.html',{'form':form, 'mensaje':mensaje})
	else:
		form = AddClienteForm(instance=cliente)
	return render(request,'users/Cliente/editCliente.html',{'form':form})

@administrador_required
def infoCliente(request, cliente_id):
	cliente = Cliente.objects.get(id = cliente_id)
	return render(request,'users/Cliente/infoCliente.html',{'cliente':cliente})

@supervisor_required
def index(request):
    return render(request,'users/Cliente/index.html')

def clienteSearch(request):
	return render(request,'users/Cliente/clienteSearch.html')

def clienteResults(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
		if search_text != '':
			clientes = Cliente.objects.filter(Q(identificacion__icontains=search_text) | Q(last_name__icontains=search_text))
			return render(request,'users/Cliente/ajax_search.html',{'clientes':clientes})
		else:
			clientes = Cliente.objects.all()
			return render(request,'users/Cliente/ajax_search.html',{'clientes':clientes})
	return render(request,'users/Cliente/ajax_search.html')
