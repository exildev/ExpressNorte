# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from domicilios.forms.users.empresaForm import AddEmpresaForm, EditEmpresaForm
from domicilios.models.users import Empresa
from domicilios.decorators import *
from django.db.models import Q

@administrador_required
def addEmpresa(request):
    if request.method == 'POST':
        form = AddEmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mensaje = {'tipo':'success','texto':"Se a registrado una empresa correctamente"}
            return render(request,'users/Empresa/index.html',{'mensaje':mensaje})
    else:
        form = AddEmpresaForm()
    return render(request,'users/Empresa/addEmpresa.html',{'form':form})

@administrador_required
def editEmpresa(request,empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    if request.method == 'POST':
        form = EditEmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            mensaje = {'tipo':'success','texto':"Se a editado una empresa correctamente"}
            form = EditEmpresaForm(instance=empresa)
            return render(request,'users/Empresa/editEmpresa.html',{'form':form, 'empresa':empresa, 'mensaje':mensaje})
    else:
        form = EditEmpresaForm(instance=empresa)
    return render(request,'users/Empresa/editEmpresa.html',{'form':form, 'empresa':empresa})

@administrador_required
def infoEmpresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    return render(request,'users/Empresa/infoEmpresa.html',{'empresa':empresa})

@administrador_required
def index(request):
    return render(request,'users/Empresa/index.html')

@administrador_required
def empresaSearch(request):
    return render(request,'users/Empresa/empresaSearch.html')

@administrador_required
def empresaResults(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text != '':
            empresasS = Empresa.objects.filter(Q(nit__icontains=search_text) | Q(first_name__icontains=search_text))
            return render(request,'users/Empresa/ajax_search.html',{'empresas':empresasS})
        else:
            empresas = Empresa.objects.all()
            return render(request,'users/Empresa/ajax_search.html',{'empresas':empresas})
    return render(request,'users/Empresa/ajax_search.html')

@administrador_required
def status(request,empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)

    if empresa.active:
        Empresa.objects.filter(id=empresa_id).update(active=False)
    else:
        Empresa.objects.filter(id=empresa_id).update(active=True)

    return redirect(reverse('domicilios:empresa_search'))
