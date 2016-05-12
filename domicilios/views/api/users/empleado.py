# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.urlresolvers import reverse
from domicilios.forms.users.empleadoForm import AddEmpleadoApiForm, EditEmpleadoApiForm, PassChangeEmpleadoForm
from domicilios.models.users import Empleado,Empresa
from domicilios.models.motorizado import *
from django.db.models import Q
from domicilios.decorators import *
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

def userEmpresa(request, num):
    user = Empleado.objects.get(username=request.user)
    empresa = Empresa.objects.get(first_name=user.empresa)
    if num == 1:
        return user
    if num == 2:
        return empresa

@administrador_required
def index(request):
    return render(request,'api/users/Empleado/index.html')

@administrador_required
def addEmpleado(request):
	print 'Llego la pelicula'
	if request.method == 'POST':
		form = AddEmpleadoApiForm(request.POST)
		if form.is_valid():
			formE = form.save(commit=False)
			formE.empresa = userEmpresa(request,2)
			formE.save()
			if request.POST.get('cargo') and 'MOTORIZADO' in request.POST['cargo']:
				return redirect(reverse('domicilios:api_add_motorizado'))
			mensaje = {'tipo':'success','texto':"Se a registrado un empleado correctamente"}
			return render(request, 'api/users/Empleado/index.html', {'mensaje':mensaje})
	else:
		form = AddEmpleadoApiForm()
	return render(request,'api/users/Empleado/addEmpleado.html',{'form':form})

@administrador_required
def empleadoSearch(request):
	return render(request,'api/users/Empleado/empleadoSearch.html')

@administrador_required
def empleadoResults(request):
	empresa = userEmpresa(request,2)
	if request.method == 'POST':
		search_text = request.POST['search_text']
		if search_text != '':
			empleados = Empleado.objects.filter(empresa=empresa).filter(Q(identificacion__icontains=search_text) | Q(last_name__icontains=search_text))
			return render(request,'api/users/Empleado/ajax_search.html',{'empleados':empleados})
		else:
			empleados = Empleado.objects.filter(empresa=empresa)
			return render(request,'api/users/Empleado/ajax_search.html',{'empleados':empleados})
	return render(request,'api/users/Empleado/ajax_search.html')

@motorizado_required
def infoEmpleado(request,empleado_id):
	empleado = get_object_or_404(Empleado, pk=empleado_id)
	if empleado.cargo == "MOTORIZADO":
		try:
			motorizado = Motorizado.objects.get(empleado = empleado_id)
			moto = Moto.objects.get(placa = motorizado.moto)
		except Exception, e:
			motorizado = 0
			moto = 0
	else:
		motorizado = False
		moto = False
	return render(request,'api/users/Empleado/infoEmpleado.html',{'empleado':empleado, 'motorizado':motorizado, 'moto':moto})

@administrador_required
def status(request,empleado_id):
	empleado = get_object_or_404(Empleado, pk=empleado_id)

	if empleado.is_active:
		Empleado.objects.filter(id=empleado_id).update(is_active=False)
	else:
		Empleado.objects.filter(id=empleado_id).update(is_active=True)

	return redirect(reverse('domicilios:api_empleado_search'))

@administrador_required
def editEmpleado(request,empleado_id):
	empleado = get_object_or_404(Empleado, pk=empleado_id)
	if request.method == 'POST':
		form = EditEmpleadoApiForm(request.POST,instance=empleado)
		if form.is_valid():
			f = form.save(commit=False)
			f.empresa = userEmpresa(request,2)
			f.save()
			mensaje = {'tipo':'success','texto':"Se a editado un empleado correctamente"}
			return render(request, 'api/users/Empleado/editEmpleado.html', {'mensaje':mensaje,'form':form, 'empleado':empleado})
	else:
		form = EditEmpleadoApiForm(instance=empleado)
	return render(request,'api/users/Empleado/editEmpleado.html',{'form':form, 'empleado':empleado})

@administrador_required
def passChangeEmpleado(request,empleado_id):
	empleado = get_object_or_404(Empleado, pk=empleado_id)
	if request.method == 'POST':
		form = PassChangeEmpleadoForm(request.POST,instance=empleado)
		if form.is_valid():
			form.save()
			mensaje = {'tipo':'success','texto':"Se a editado la contraseña un empleado correctamente"}
			return render(request, 'api/users/Empleado/passChangeEmpleado.html', {'mensaje':mensaje, 'form':form, 'empleado':empleado})
	else:
		form = PassChangeEmpleadoForm(instance=empleado)
	return render(request,'api/users/Empleado/passChangeEmpleado.html',{'form':form, 'empleado':empleado})


@csrf_exempt
def searchEmpleadoTabla(request):
    length=request.GET.get('length','0')
    columnas = ['nombre','descripcion']
    num_columno = request.GET.get('order[0][column]','0')
    order = request.GET.get('order[0][dir]',0)
    busqueda = request.GET.get('columns[1][search][value]','')
    start  = request.GET.get('start',0)
    search = request.GET.get('search[value]',False)
    cursor = connection.cursor()
    cursor.execute('select tabla_empleado(%d,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer)'%(request.user.id,busqueda,order,start,length))
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def

