# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from domicilios.forms.users.empleadoForm import AddEmpleadoForm, EditEmpleadoForm, PassChangeEmpleadoForm
from domicilios.models.users import Empleado
from domicilios.models.motorizado import *
from django.db.models import Q
from domicilios.decorators import *


@administrador_required
def addEmpleado(request):
    print 'Llegando a el empleado'
    if request.method == 'POST':
        form = AddEmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get('cargo') and 'MOTORIZADO' in request.POST['cargo']:
                return redirect(reverse('domicilios:add_motorizado'))
            mensaje = {'tipo': 'success', 'texto': "Se a registrado un empleado correctamente"}
            return render(request, 'users/Empleado/index.html', {'mensaje': mensaje})
    else:
        form = AddEmpleadoForm()
    return render(request, 'users/Empleado/addEmpleado.html', {'form': form})


@motorizado_required
def infoEmpleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if empleado.cargo == "MOTORIZADO":
        try:
            motorizado = Motorizado.objects.get(empleado=empleado_id)
            moto = Moto.objects.get(placa=motorizado.moto)
        except Exception, e:
            motorizado = 0
            moto = 0
    else:
        motorizado = False
        moto = False
    return render(request, 'users/Empleado/infoEmpleado.html',
                  {'empleado': empleado, 'motorizado': motorizado, 'moto': moto})


@administrador_required
def status(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)

    if empleado.is_active:
        Empleado.objects.filter(id=empleado_id).update(is_active=False)
    else:
        Empleado.objects.filter(id=empleado_id).update(is_active=True)

    return redirect(reverse('domicilios:empleado_search'))

@administrador_required
def editEmpleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == 'POST':
        form = EditEmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            mensaje = {'tipo': 'success', 'texto': "Se a editado un empleado correctamente"}
            form = EditEmpleadoForm(instance=empleado)
            return render(request, 'users/Empleado/editEmpleado.html', {'form': form, 'empleado': empleado, 'mensaje': mensaje})
    else:
        form = EditEmpleadoForm(instance=empleado)
    return render(request, 'users/Empleado/editEmpleado.html', {'form': form, 'empleado': empleado})


@administrador_required
def passChangeEmpleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == 'POST':
        form = PassChangeEmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            mensaje = {'tipo': 'success', 'texto': "Se a editado la contraseña un empleado correctamente"}
            form = PassChangeEmpleadoForm(instance=empleado)
            return render(request, 'users/Empleado/passChangeEmpleado.html', {'form': form, 'empleado': empleado, 'mensaje': mensaje})
    else:
        form = PassChangeEmpleadoForm(instance=empleado)
    return render(request, 'users/Empleado/passChangeEmpleado.html', {'form': form, 'empleado': empleado})


@administrador_required
def empleadoSearch(request):
    return render(request, 'users/Empleado/empleadoSearch.html')


@administrador_required
def empleadoResults(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text != '':
            empleados = Empleado.objects.filter(
                Q(identificacion__icontains=search_text) | Q(last_name__icontains=search_text))
            return render(request, 'users/Empleado/ajax_search.html', {'empleados': empleados})
        else:
            empleados = Empleado.objects.all()
            return render(request, 'users/Empleado/ajax_search.html', {'empleados': empleados})
    return render(request, 'users/Empleado/ajax_search.html')


@administrador_required
def index(request):
    return render(request, 'users/Empleado/index.html')
