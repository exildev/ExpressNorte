# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect,HttpResponse,get_object_or_404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from domicilios.forms.pedido.pedidoForm import *
from domicilios.forms.users.clienteForm import *
from domicilios.models.users import Empleado, Empresa
from domicilios.models.motorizado import *
from domicilios.decorators import *
from domicilios.models.pedido import Pedido, ItemsPedido, Items, Tiempo
from django.utils import timezone
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


@motorizado_required
def userEmpresa(request, num):
    user = Empleado.objects.get(username=request.user)
    empresa = Empresa.objects.get(first_name=user.empresa)
    if num == 1:
        return user
    if num == 2:
        return empresa

@motorizado_required
def index(request):
    return render(request, 'pedidos/index.html')

@motorizado_required
def addItems(request):
    print 'esto son los pedidos 2'
    if request.method == 'POST':
        form = AddItemsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.empresaI = userEmpresa(request,2)
            f.status = True
            f.save()
            mensaje = {'tipo': 'success', 'texto': 'El item se agregó correctamente'}
            form = AddItemsForm()
            return render(request, 'pedidos/addItems.html', {'form': form, 'mensaje':mensaje})
    else:
        form = AddItemsForm()
    return render(request, 'pedidos/addItems.html', {'form': form})

@motorizado_required
def editItems(request,item_id):
    item = get_object_or_404(Items,pk=item_id)
    if request.method == 'POST':
        form = AddItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            mensaje = {'tipo':'success', 'texto':'El item se actualizó correctamente'}
            return render(request,'pedidos/editItems.html',{'mensaje':mensaje,'form':form})
    else:
        form = AddItemsForm(instance=item)
    return render(request,'pedidos/editItems.html',{'form':form})

@motorizado_required
def listItems(request):
    return render(request,'pedidos/itemsSearch.html')

def deleteItems(request,item_id):
    item = get_object_or_404(Items, pk=item_id)

    if item.status:
        Items.objects.filter(id=item_id).update(status=False)
    else:
        Items.objects.filter(id=item_id).update(status=True)

    return redirect(reverse('domicilios:list_items'))

@motorizado_required
def listItemsResults(request):
    empresa = userEmpresa(request,2)
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text != '':
            items = Items.objects.filter(codigo__icontains=search_text)
            return render(request,'pedidos/itemsResults.html', {'items':items})
        else:
            items = Items.objects.all()
            return render(request,'pedidos/itemsResults.html', {'items':items})


def pedidoSearch(request):
    return render(request,'pedidos/pedidosSearch.html')

def pedidoResults(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text != '':
            pedidos = Pedido.objects.filter(num_pedido__icontains=search_text).order_by("-id")
            return render(request,'pedidos/ajax_pedido.html',{'pedidos':pedidos})
        else:
            pedidos = Pedido.objects.all().order_by("-id")
    return render(request,'pedidos/ajax_pedido.html',{'pedidos':pedidos})

@motorizado_required
def infoPedido(request,pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    items = ItemsPedido.objects.filter(pedido=pedido_id)
    tiempos= Tiempo.objects.get(pedido=pedido)
    try:
        certificado = Certificado.objects.get(pedidoC=pedido)
        return render(request,'pedidos/infoPedido.html',{'pedido':pedido,'items':items,'tiempos':tiempos,'certificado':certificado})
    except Exception, e:
        return render(request,'pedidos/infoPedido.html',{'pedido':pedido,'items':items,'tiempos':tiempos,})

@motorizado_required
def misPedidos(request):
    user = Empleado.objects.get(username=request.user)
    if user.cargo == 'SUPERVISOR' or user.cargo == 'ADMINISTRADOR':
        pedidos = Pedido.objects.filter(supervisor=request.user).order_by("-id")
        return render(request,'pedidos/misPedidos.html',{'pedidos':pedidos})
    elif user.cargo == 'ALISTADOR':
        pedidos = Pedido.objects.filter(alistador=request.user).order_by("-id")
        return render(request,'pedidos/misPedidos.html',{'pedidos':pedidos})
    else:
        pedidos = Pedido.objects.filter(motorizado=request.user).order_by("-id")
        return render(request,'pedidos/misPedidos.html',{'pedidos':pedidos})

@motorizado_required
def asignarMotorizado(request):
    pedido = Pedido.objects.exclude(motorizado__isnull=False)
    cont = 0
    for x in pedido:
        if not x.motorizado:
            cont += 1
    if cont == 0:
        return render(request,'pedidos/asignarMotorizado.html')
    else:
        return render(request,'pedidos/asignarMotorizado.html',{'pedido':pedido})

@motorizado_required
def chooseMotorizado(request, pedido_id):
    motorizados = Motorizado.objects.all()
    return render(request,'pedidos/chooseMotorizado.html',{'motorizados':motorizados, 'pedido':pedido_id})

@motorizado_required
def finalizarPedido(request):
    pedido = Pedido.objects.exclude(motorizado__isnull=False)
    if request.method == "POST":
        pedido_id = request.POST['pedido']
        motorizado = request.POST['motorizado']
        motorizadoPedido = Empleado.objects.get(identificacion=motorizado)
        pedidoUpdate = Pedido.objects.filter(id=pedido_id)
        pedidoUpdate.update(motorizado=motorizadoPedido)
        Tiempo.objects.filter(pedido=pedidoUpdate).update(tiempo_asignacion=timezone.now())
        mensaje = {'tipo':'success','texto':'Se asignó el motorizado correctamente'}
        return render(request,'pedidos/asignarMotorizado.html',{'mensaje':mensaje,'pedido':pedido})

@motorizado_required
def addPedido(request):
    p = Pedido.objects.all().count()
    c = False
    if p > 0:
        c = True
    else:
        c = False

    if request.method == 'POST':
        formC = AddClienteForm(request.POST)
        formP = AddPedidoForm(request.POST)
        if formC.is_valid():
            formC.save()
            return redirect(reverse('domicilios:add_pedido'))
        else:
            if formP.is_valid():
                fp = formP.save(commit=False)
                if c == False:
                    fp.npedido_express = 'EX_1'
                else:
                    npedido = Pedido.objects.latest("id")
                    a = npedido.npedido_express
                    a = a.split("EX_")
                    n = int(a[1])
                    n = "EX_" + str(n+1)
                    fp.npedido_express = n
                newPedido = formP.save()
                formTiempo = AddTiempoForm(instance=Tiempo())
                newTiempo = formTiempo.save(commit=False)
                newTiempo.pedido = newPedido
                newTiempo.tiempo_pedido = timezone.now()
                newTiempo.save()
                return redirect(reverse('domicilios:add_pedido_items'))
    else:
        formC = AddClienteForm()
        formP = AddPedidoForm()
    return render(request, 'pedidos/addPedido.html', {'formC': formC, 'formP': formP})

@motorizado_required
def pedidoItems(request):
    total = 0
    pedido = Pedido.objects.latest("id")
    try:
        items = ItemsPedido.objects.filter(pedido=pedido.id).select_related('item')
        for x in items:
            total += x.valor_total
        if request.method == 'POST':
            formItems = AddItemsPedidoForm(request.POST)
            if formItems.is_valid():
                formI = formItems.save(commit=False)
                formI.pedido = pedido
                formI.valor_total = formI.cantidad * formI.valor_unitario
                formI.save()
                return redirect(reverse('domicilios:add_pedido_items'))
        else:
            formItems = AddItemsPedidoForm()
        return render(request, 'pedidos/pedidoItems.html',
                      {'pedido': pedido, 'form': formItems, 'items': items, 'total': total})
    except Exception, e:
        formItems = AddItemsPedidoForm()
        formItems.fields["item"].queryset = Items.objects.filter(empresaI=userEmpresa(request,2))
        return render(request, 'pedidos/pedidoItems.html', {'pedido': pedido, 'form': formItems, 'total': total})

def addItemPedido(request):
    if request.method == 'POST':
        form = AddItemsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.empresaI = userEmpresa(request,2)
            f.save()
            return redirect(reverse('domicilios:add_pedido_items'))
    else:
        form = AddItemsForm()
    return render(request, 'pedidos/addItemPedido.html', {'form': form})


def totalPedido(request):
    pedido = Pedido.objects.latest("id")
    if request.method == 'POST':
        pedido = request.POST['pedido']
        pedidoB = Pedido.objects.get(id=pedido)
        total = 0
        items = ItemsPedido.objects.filter(pedido=pedidoB)
        for x in items:
            total += x.valor_total

        if total > 0:
            Pedido.objects.filter(id=pedido).update(total=total)
            formC = AddClienteForm()
            formP = AddPedidoForm()
            formA = AddPedidoAdminForm()
            mensaje = {'tipo':'success', 'texto': 'El pedido a sido guardado exitosamente'}
            pedidoF = Pedido.objects.latest("id")
            if pedidoF.motorizado:
                return render(request, 'pedidos/addPedidoAdmin.html', {'formC': formC, 'formP': formA, 'mensaje':mensaje})
            else:
                #return render(request, 'pedidos/addPedido.html', {'formC': formC, 'formP': formP, 'mensaje':mensaje})
                return HttpResponseRedirect('/plataforma/pedido/')
        else:
            formItems = AddItemsPedidoForm()
            pedido = Pedido.objects.latest("id")
            error = "no puedes dejar el pedido sin items"
            return render(request, 'pedidos/pedidoItems.html',
                          {'pedido': pedido, 'form': formItems, 'items': items, 'total': total, 'error': error})

@motorizado_required
def deletePedidoItems(request, item_id):
    item = ItemsPedido.objects.get(id=item_id)
    item.delete()
    return redirect(reverse('domicilios:add_pedido_items'))

from easy_pdf.views import PDFTemplateView

class facturaPedido(PDFTemplateView):
    template_name = "pedidos/factura.html"

    def get_context_data(self, pedido_id, **kwargs):

        pedido = get_object_or_404(Pedido,id=pedido_id)
        items = ItemsPedido.objects.filter(pedido=pedido)
        empresa = Empresa.objects.get(first_name=pedido.empresa)
        cliente = Cliente.objects.get(identificacion=pedido.cliente)
        return super(facturaPedido, self).get_context_data(
            pagesize="A5",
            title="Pedido",
            pedido=pedido, items=items, empresa=empresa, cliente=cliente,
            **kwargs
        )

@motorizado_required
def pedidoCertificado(request):
    count = Pedido.objects.filter(certificado__pedidoC__isnull=True).filter(motorizado=userEmpresa(request,1)).count()
    if count > 0:
        if request.method == 'POST':
            formC = CertificadoForm(request.POST, request.FILES)
            if formC.is_valid():
                form = formC.save(commit=False)
                pedido = Pedido.objects.get(npedido_express=form.pedidoC)
                cliente = Cliente.objects.get(identificacion=pedido.cliente)
                form.clienteC = cliente
                Tiempo.objects.filter(pedido=pedido).update(tiempo_entrego=timezone.now())
                form.save()
                mensaje = {'tipo':'success', 'texto':'Pedido certificado correctamente'}
                formC = CertificadoForm()
                formC.fields["pedidoC"].queryset = Pedido.objects.filter(certificado__pedidoC__isnull=True).filter(motorizado=userEmpresa(request,1))
                return render(request,'pedidos/pedidoCertificado.html',{'form':formC,'mensaje':mensaje})
        else:
            formC = CertificadoForm()
            formC.fields["pedidoC"].queryset = Pedido.objects.filter(certificado__pedidoC__isnull=True).filter(motorizado=userEmpresa(request,1))
        return render(request,'pedidos/pedidoCertificado.html',{'form':formC})
    else:
        return render(request,'pedidos/pedidoCertificado.html')

# view para añadir pedido desde la interfaz de administrador

@motorizado_required
def addPedidoAdmin(request):
    p = Pedido.objects.all().count()
    c = False
    if p > 0:
        c = True
    else:
        c = False

    if request.method == 'POST':
        formC = AddClienteForm(request.POST)
        formP = AddPedidoAdminForm(request.POST)
        if formC.is_valid():
            formC.save()
            return redirect(reverse('domicilios:add_pedido_admin'))
        else:
            if formP.is_valid():
                fp = formP.save(commit=False)
                if c == False:
                    fp.npedido_express = 'EX_1'
                else:
                    npedido = Pedido.objects.latest("id")
                    a = npedido.npedido_express
                    a = a.split("EX_")
                    n = int(a[1])
                    n = "EX_" + str(n+1)
                    fp.npedido_express = n
                newPedido = formP.save()
                formTiempo = AddTiempoForm(instance=Tiempo())
                newTiempo = formTiempo.save(commit=False)
                newTiempo.pedido = newPedido
                newTiempo.tiempo_pedido = timezone.now()
                newTiempo.tiempo_asignacion = timezone.now()
                newTiempo.save()
                return redirect(reverse('domicilios:add_pedido_items'))
    else:
        formC = AddClienteForm()
        formP = AddPedidoAdminForm()
    return render(request, 'pedidos/addPedidoAdmin.html', {'formC': formC, 'formP': formP})

@motorizado_required
def editPedido(request,pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedidoForm = AddPedidoAdminForm(request.POST, instance=pedido)
        if pedidoForm.is_valid():
            pedidoForm.save()
            return HttpResponseRedirect('/pedido/%s/edit/items/' % pedido.id)
    else:
        pedidoForm = AddPedidoAdminForm(instance=pedido)
    return render(request,'pedidos/editPedido.html', {'pedidoForm':pedidoForm})

@motorizado_required
def editPedidoItems(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    total = 0
    items = ItemsPedido.objects.filter(pedido=pedido.id).select_related('item')
    for x in items:
        total += x.valor_total
    if request.method == 'POST':
        formItems = AddItemsPedidoForm(request.POST)
        if formItems.is_valid():
            formI = formItems.save(commit=False)
            formI.pedido = pedido
            formI.valor_total = formI.cantidad * formI.valor_unitario
            formI.save()
            return HttpResponseRedirect('/pedido/%s/edit/items/' % pedido.id)
    else:
        formItems = AddItemsPedidoForm()
    return render(request, 'pedidos/editPedidoItems.html',
                  {'pedido': pedido, 'form': formItems, 'items': items, 'total': total})

@motorizado_required
def deletePedidoItemsEdit(request, item_id):
    item = ItemsPedido.objects.get(id=item_id)
    item.delete()
    return HttpResponseRedirect('/pedido/%s/edit/items/' % item.pedido.id)

@motorizado_required
def totalPedidoEdit(request):
    if request.method == 'POST':
        pedido = request.POST['pedido']
        pedidoB = Pedido.objects.get(id=pedido)
        total = 0
        items = ItemsPedido.objects.filter(pedido=pedidoB)
        for x in items:
            total += x.valor_total

        if total > 0:
            Pedido.objects.filter(id=pedido).update(total=total)
            return redirect(reverse('domicilios:pedido_search'))
        else:
            formItems = AddItemsPedidoForm()
            pedido = Pedido.objects.latest("id")
            mensaje = {'tipo':'success', 'texto':'no puedes dejar el pedido sin items'}
            return render(request, 'pedidos/editPedidoItems.html',
                          {'pedido': pedido, 'form': formItems, 'items': items, 'total': total, 'mensaje': mensaje})

def comprobar_pedido(request, pedido_id):
    try:
        pedido = Pedido.objects.get(num_pedido = pedido_id)
    except Pedido.DoesNotExist:
        pedido = None
    data = {}
    if pedido != None:
        try:
            certificado = Certificado.objects.get(pedidoC=pedido)
        except Certificado.DoesNotExist:
            certificado = None
        if certificado == None:
            motorizado = Motorizado.objects.get(empleado = pedido.motorizado)
            data['status'] = "success"
            data['key'] = motorizado.identifier
        else:
            data['status'] = "finish"
    else:
        data['status'] = "error"
    response = HttpResponse(json.dumps(data))
    response.__setitem__("Content-type", "application/json")
    response.__setitem__("Access-Control-Allow-Origin", "*")

    return response

@csrf_exempt
def searchTablaPedidos(request):
    length=request.GET.get('length','0')
    columnas = ['nombre','descripcion']
    num_columno = request.GET.get('order[0][column]','0')
    order = request.GET.get('order[0][dir]',0)
    busqueda = request.GET.get('columns[1][search][value]','')
    start  = request.GET.get('start',0)
    search = request.GET.get('search[value]',False)
    cursor = connection.cursor()
    cursor.execute('select tabla_pedidos(%d,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer)'%(request.user.id,busqueda,order,start,length))
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def

