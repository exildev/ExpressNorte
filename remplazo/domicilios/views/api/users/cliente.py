from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from domicilios.forms.users.clienteForm import AddClienteForm
from domicilios.models.users import Cliente
from django.db.models import Q
from domicilios.decorators import *
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

def index(request):
    return render(request,'api/users/Cliente/index.html')

@supervisor_required
def addCliente(request):
	if request.method == 'POST':
		form = AddClienteForm(request.POST)
		if form.is_valid():
			form.save()
			mensaje = {'tipo':'success','texto':"Se a registrado un cliente correctamente"}
			return render(request, 'api/users/Cliente/index.html', {'mensaje':mensaje})
	else:
		form = AddClienteForm()
	return render(request,'api/users/Cliente/addCliente.html',{'form':form})

def clienteSearch(request):
	return render(request,'api/users/Cliente/clienteSearch.html')

def clienteResults(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
		if search_text != '':
			clientes = Cliente.objects.filter(Q(identificacion__icontains=search_text) | Q(last_name__icontains=search_text))
			return render(request,'api/users/Cliente/ajax_search.html',{'clientes':clientes})
		else:
			clientes = Cliente.objects.all()
			return render(request,'api/users/Cliente/ajax_search.html',{'clientes':clientes})
	return render(request,'api/users/Cliente/ajax_search.html')

@administrador_required
def infoCliente(request, cliente_id):
	cliente = Cliente.objects.filter(id = cliente_id).first()
	if cliente :
		return render(request,'api/users/Cliente/infoCliente.html',{'cliente':cliente})
	#end if
	return HttpResponseRedirect('/')
	

@administrador_required
def editCliente(request,cliente_id):
	cliente = Cliente.objects.get(id = cliente_id)
	if request.method == 'POST':
		form = AddClienteForm(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
			mensaje = {'tipo':'success','texto':"Se a editado un cliente correctamente"}
			return render(request, 'api/users/Cliente/editCliente.html', {'mensaje':mensaje,'form':form})
	else:
		form = AddClienteForm(instance=cliente)

	return render(request,'api/users/Cliente/editCliente.html',{'form':form})


@csrf_exempt
def searchCliente(request):
	print request.GET,request.GET.get('search[value]',False)
	length=request.GET.get('length')
	columnas = ['nombre','descripcion']
	num_columno = request.GET.get('order[0][column]','0')
	order = request.GET.get('order[0][dir]',0)
	start  = request.GET.get('start',0)
	search = request.GET.get('search[value]',False)
	busqueda = request.GET.get('columns[1][search][value]','')
	cursor = connection.cursor()
	cursor.execute('select tabla_cliente(%d,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer)'%(request.user.id,busqueda,order,start,length))
	row = cursor.fetchone()
	return HttpResponse(row[0],content_type="application/json")
#end def