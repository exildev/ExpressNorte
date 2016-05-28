# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from domicilios.forms.pedido.pedidoForm import *
from domicilios.forms.users.clienteForm import *
from domicilios.models.users import Empleado, Empresa, Cliente
from domicilios.models.motorizado import *
from domicilios.models.pedido import Pedido, ItemsPedido, Items
from domicilios.decorators import *
from django.utils import timezone
from django.db.models import Q,Sum
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.core.exceptions import PermissionDenied
import json

def userEmpresa(request, num):
    user = Empleado.objects.get(username=request.user)
    empresa = Empresa.objects.get(first_name=user.empresa)
    if num == 1:
        return user
    if num == 2:
        return empresa

def index(request):
    return render(request, 'api/pedidos/index.html')

def addItems(request):
    if request.method == 'POST':
        form = AddItemsApiForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.empresaI = userEmpresa(request,2)
            f.save()
            mensaje = {'tipo': 'success', 'texto': 'El item se agregó correctamente'}
            return render(request, 'api/pedidos/addItems.html', {'form': form, 'mensaje':mensaje})
    else:
        form = AddItemsApiForm()
    return render(request, 'api/pedidos/addItems.html', {'form': form})

def listItems(request):
    return render(request,'api/pedidos/itemsSearch.html')

def listItemsResults(request):
    empresa = userEmpresa(request,2)
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text != '':
            items = Items.objects.filter(codigo__icontains=search_text).filter(empresaI=empresa)
            return render(request,'api/pedidos/itemsResults.html', {'items':items})
        else:
            items = Items.objects.filter(empresaI=empresa)
            return render(request,'api/pedidos/itemsResults.html', {'items':items})


def pedidoSearch(request):
    return render(request,'api/pedidos/pedidosSearch.html')

def pedidoResults(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text != '':
            pedidos = Pedido.objects.filter(empresa=userEmpresa(request,2)).filter(num_pedido__icontains=search_text).order_by("-id")
            return render(request,'api/pedidos/ajax_pedido.html',{'pedidos':pedidos})
        else:
            pedidos = Pedido.objects.filter(empresa=userEmpresa(request,2)).order_by("-id")
    return render(request,'api/pedidos/ajax_pedido.html',{'pedidos':pedidos})


def infoPedido(request,pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    items = ItemsPedido.objects.filter(pedido=pedido_id)
    tiempos= Tiempo.objects.get(pedido=pedido)
    try:
        certificado = Certificado.objects.get(pedidoC=pedido)
        return render(request,'api/pedidos/infoPedido.html',{'pedido':pedido,'items':items,'tiempos':tiempos,'certificado':certificado})
    except Exception, e:
        return render(request,'api/pedidos/infoPedido.html',{'pedido':pedido,'items':items,'tiempos':tiempos})

def misPedidos(request):
    user = Empleado.objects.filter(username=request.user).first()
    print user.id
    if user:
        if user.cargo == 'SUPERVISOR' or user.cargo == 'ADMINISTRADOR':
            pedidos = Pedido.objects.filter(supervisor=request.user).order_by("-id")
            return render(request,'api/pedidos/misPedidos.html',{'pedidos':pedidos})
        elif user.cargo == 'ALISTADOR':
            pedidos = Pedido.objects.filter(alistador=request.user).order_by("-id")
            return render(request,'api/pedidos/misPedidos.html',{'pedidos':pedidos})
        else:
            return render(request,'api/pedidos/pedidosmotorizado.html')
    else:
        raise PermissionDenied
    #end if

def asignarMotorizado(request):
    pedido = Pedido.objects.filter(alistador=request.user)
    cont = 0
    for x in pedido:
        if not x.motorizado:
            cont += 1

    if cont == 0:
        return render(request,'api/pedidos/asignarMotorizado.html')
    else:
        return render(request,'api/pedidos/asignarMotorizado.html',{'pedido':pedido})

def chooseMotorizado(request, pedido_id):
    express = Empresa.objects.filter(username="express")
    motorizados = Motorizado.objects.filter(empleado__empresa=userEmpresa(request,2))
    motorizadosE = Motorizado.objects.filter(empleado__empresa=express)
    return render(request,'api/pedidos/chooseMotorizado.html',{'motorizados':motorizados, 'motorizadosE':motorizadosE, 'pedido':pedido_id})

def finalizarPedido(request):
    pedido = Pedido.objects.filter(alistador=request.user)
    if request.method == "POST":
        pedido_id = request.POST['pedido']
        motorizado = request.POST['motorizado']
        motorizadoPedido = Empleado.objects.get(identificacion=motorizado)
        pedidoUpdate = Pedido.objects.filter(num_pedido=pedido_id)
        pedidoUpdate.update(motorizado=motorizadoPedido)
        Tiempo.objects.filter(pedido=pedidoUpdate).update(tiempo_asignacion=timezone.now())
        mensaje = {'tipo':'success','texto':'Se asignó el motorizado correctamente'}
        return render(request,'api/pedidos/asignarMotorizado.html',{'mensaje':mensaje,'pedido':pedido})

def addPedido(request):
    p = Pedido.objects.all().count()
    c = False
    if p > 0:
        c = True
    else:
        c = False

    if request.method == 'POST':
        formC = AddClienteForm(request.POST)
        formP = AddPedidoApiForm(request.POST)
        if formC.is_valid():
            formC.save()
            return redirect(reverse('domicilios:api_add_pedido'))
        else:
            if formP.is_valid():
                form = formP.save(commit=False)
                form.supervisor = userEmpresa(request,1)
                form.empresa = userEmpresa(request,2)
                if c == False:
                    form.npedido_express = 'EX_1'
                else:
                    npedido = Pedido.objects.latest("id")
                    a = npedido.npedido_express
                    a = a.split("EX_")
                    n = int(a[1])
                    n = "EX_" + str(n+1)
                    form.npedido_express = n
                form.save()
                formTiempo = AddTiempoForm(instance=Tiempo())
                newTiempo = formTiempo.save(commit=False)
                pedido = Pedido.objects.latest("id")
                newTiempo.pedido = pedido
                newTiempo.tiempo_pedido = timezone.now()
                newTiempo.save()
                return redirect(reverse('domicilios:api_add_pedido_items'))
    else:
        formC = AddClienteForm()
        formP = AddPedidoApiForm()
        formP.fields["alistador"].queryset = Empleado.objects.filter(cargo="ALISTADOR").filter(empresa=userEmpresa(request,2))
    return render(request, 'api/pedidos/addPedido.html', {'formC': formC, 'formP': formP})



def pedidoItems(request):
    total = 0
    pedido = Pedido.objects.latest("id")
    if pedido :
        items = ItemsPedido.objects.filter(pedido=pedido.id).select_related('item')
        if items :
            resul = items.aggregate(suma=Sum('valor_total'))
            total= resul['suma'] if resul['suma'] is not None else 0
        #end if
        if request.method == 'POST':
            formItems = AddItemsPedidoForm(request.POST)
            if formItems.is_valid():
                formI = formItems.save(commit=False)
                formI.pedido = pedido
                formI.valor_total = formI.valor_unitario * formI.cantidad
                formI.save()
                return redirect(reverse('domicilios:api_add_pedido_items'))
            #end if
        else:
            formItems = AddItemsPedidoForm()
            formItems.fields["item"].queryset = Items.objects.filter(empresaI=userEmpresa(request,2))
        return render(request, 'api/pedidos/pedidoItems.html',
                      {'pedido': pedido, 'form': formItems, 'items': items, 'total': total})
    #end if
    formItems = AddItemsPedidoForm()
    formItems.fields["item"].queryset = Items.objects.filter(empresaI=userEmpresa(request,2))
    return render(request, 'api/pedidos/pedidoItems.html', {'pedido': pedido, 'form': formItems, 'total': total})

def addItemPedido(request):
    if request.method == 'POST':
        form = AddItemsApiForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.empresaI = userEmpresa(request,2)
            f.save()
            return redirect(reverse('domicilios:api_add_pedido_items'))
    else:
        form = AddItemsApiForm()
    return render(request, 'api/pedidos/addItemPedido.html', {'form': form})


def totalPedido(request):
    print '¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨',request.POST
    if request.method == 'POST':
        pedido = request.POST.get('pedido',False)
        if pedido :
            pedidoB = Pedido.objects.filter(npedido_express=pedido).first()
            if pedidoB :
                total = 0
                items = ItemsPedido.objects.filter(pedido=pedidoB)
                if items :
                    resul = items.aggregate(suma=Sum('valor_total'))
                    total = resul['suma'] if resul['suma'] is not None else 0
                    if total > 0:
                        p = Pedido.objects.filter(npedido_express=pedido)
                        if p :
                            Pedido.objects.filter(npedido_express=pedido).update(total=total,confirmado=True)
                            formC = AddClienteForm()
                            formP = AddPedidoForm()
                            formA = AddPedidoAdminApiForm()
                            mensaje = {'tipo':'success', 'texto': 'El pedido a sido guardado exitosamente'}
                            if p[0].motorizado:
                                return HttpResponseRedirect('/plataforma/pedido/')
                                return render(request, 'api/pedidos/addPedidoAdmin.html', {'formC': formC, 'formP': formA, 'mensaje':mensaje})
                            else:
                                #return render(request, 'api/pedidos/addPedido.html', {'formC': formC, 'formP': formP, 'mensaje':mensaje})
                                return HttpResponseRedirect('/plataforma/pedido/')
                        #end if
                    else:
                        formItems = AddItemsPedidoForm()
                        pedido = Pedido.objects.latest("id")
                        error = "no puedes dejar el pedido sin items"
                        return render(request, 'api/pedidos/pedidoItems.html',
                                      {'pedido': pedido, 'form': formItems, 'items': items, 'total': total, 'error': error})
                #end if
            #end if
        #end if
    #end if
    return HttpResponseRedirect('/plataforma/pedido/')

def deletePedidoItems(request, item_id):
    item = ItemsPedido.objects.filter(id=item_id)
    if item :
        item.delete()
        return redirect(reverse('domicilios:api_add_pedido_items'))
    #end if
    return render(request, 'api/pedidos/index.html')

def editItems(request,item_id):
    item = get_object_or_404(Items,pk=item_id)
    if request.method == 'POST':
        form = AddItemsApiForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            mensaje = {'tipo':'success', 'texto':'El item se actualizó correctamente'}
            return render(request,'api/pedidos/editItems.html',{'mensaje':mensaje,'form':form})
    else:
        form = AddItemsApiForm(instance=item)
    return render(request,'api/pedidos/editItems.html',{'form':form})

from easy_pdf.views import PDFTemplateView

class facturaPedido(PDFTemplateView):
    template_name = "api/pedidos/factura.html"

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



def pedidoCertificado(request):
    count = Pedido.objects.filter(certificado__pedidoC__isnull=True).count()
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
                return render(request,'api/pedidos/pedidoCertificado.html',{'form':formC,'mensaje':mensaje})
        else:
            formC = CertificadoForm()
            formC.fields["pedidoC"].queryset = Pedido.objects.filter(certificado__pedidoC__isnull=True).filter(motorizado=userEmpresa(request,1))
        return render(request,'api/pedidos/pedidoCertificado.html',{'form':formC})
    else:
        return render(request,'api/pedidos/pedidoCertificado.html')

# vista para añadir un pedido con la interfaz de administrador
def addPedidoAdmin(request):
    p = Pedido.objects.all().count()
    c = False
    if p > 0:
        c = True
    else:
        c = False

    if request.method == 'POST':
        formC = AddClienteForm(request.POST)
        formP = AddPedidoAdminApiForm(request.POST)
        m = request.POST["motorizado"]
        if formC.is_valid():
            formC.save()
            return redirect(reverse('domicilios:api_add_pedido_admin'))
        else:
            if formP.is_valid():
                form = formP.save(commit=False)
                form.empresa = userEmpresa(request,2)
                if c == False:
                    form.npedido_express = 'EX_1'
                else:
                    npedido = Pedido.objects.latest("id")
                    a = npedido.npedido_express
                    a = a.split("EX_")
                    n = int(a[1])
                    n = "EX_" + str(n+1)
                    form.npedido_express = n
                motorizado = Empleado.objects.get(identificacion=m)
                form.motorizado = motorizado
                form.save()
                formTiempo = AddTiempoForm(instance=Tiempo())
                newTiempo = formTiempo.save(commit=False)
                pedido = Pedido.objects.latest("id")
                newTiempo.pedido = pedido
                newTiempo.tiempo_pedido = timezone.now()
                newTiempo.tiempo_asignacion = timezone.now()
                newTiempo.save()
                return redirect(reverse('domicilios:api_add_pedido_items'))
    else:
        formC = AddClienteForm()
        formP = AddPedidoAdminApiForm()
        formP.fields["alistador"].queryset = Empleado.objects.filter(cargo="ALISTADOR").filter(empresa=userEmpresa(request,2))
        formP.fields["supervisor"].queryset = Empleado.objects.filter(cargo="SUPERVISOR").filter(empresa=userEmpresa(request,2))
        motorizados = Motorizado.objects.filter(empleado__empresa=userEmpresa(request,2))
        express = Empresa.objects.filter(username="express")
        motorizadosE = Motorizado.objects.filter(empleado__empresa=express)
    return render(request, 'api/pedidos/addPedidoAdmin.html', {'formC': formC, 'formP': formP,'motorizados':motorizados,'motorizadosE':motorizadosE})


def editPedido(request,pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedidoForm = EditPedidoAdminApiForm(request.POST, instance=pedido)
        if pedidoForm.is_valid():
            f = pedidoForm.save(commit=False)
            f.empresa = userEmpresa(request,2)
            f.save()
            return HttpResponseRedirect('/plataforma/pedido/%s/edit/items/' % pedido.id)
    else:
        pedidoForm = EditPedidoAdminApiForm(instance=pedido)
        pedidoForm.fields["alistador"].queryset = Empleado.objects.filter(cargo="ALISTADOR").filter(empresa=userEmpresa(request,2))
        pedidoForm.fields["supervisor"].queryset = Empleado.objects.filter(cargo="SUPERVISOR").filter(empresa=userEmpresa(request,2))
        pedidoForm.fields["motorizado"].queryset = Empleado.objects.filter(cargo="MOTORIZADO").filter(empresa=userEmpresa(request,2))
    return render(request,'api/pedidos/editPedido.html', {'pedidoForm':pedidoForm})

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
            return HttpResponseRedirect('/plataforma/pedido/%s/edit/items/' % pedido.id)
    else:
        formItems = AddItemsPedidoForm()
        formItems.fields["item"].queryset = Items.objects.filter(empresaI=userEmpresa(request,2))
    return render(request, 'api/pedidos/editPedidoItems.html',
                  {'pedido': pedido, 'form': formItems, 'items': items, 'total': total})

def deletePedidoItemsEdit(request, item_id):
    item = ItemsPedido.objects.filter(id=item_id)
    if item :
        item.delete()
        return HttpResponseRedirect('/plataforma/pedido/%s/edit/items/' % item.pedido.id)
    #end def
    return redirect(reverse('domicilios:api_add_pedido_items'))

def totalPedidoEdit(request):
    if request.method == 'POST':
        pedido = request.POST['pedido']
        pedidoB = Pedido.objects.filter(id=pedido).first()
        if pedidoB :
            resul = ItemsPedido.objects.filter(pedido=pedidoB).aggregate(suma=Sum('valor_total'))
            total = resul['suma'] if resul['suma'] is not None else 0
            if total > 0:
                Pedido.objects.filter(id=pedido).update(total=total)
                return redirect(reverse('domicilios:api_pedido_search'))
            else:
                formItems = AddItemsPedidoForm()
                error = "no puedes dejar el pedido sin items"
                return render(request, 'api/pedidos/pedidoItems.html',
                              {'pedido': pedidoB, 'form': formItems, 'items': items, 'total': total, 'error': error})
            #end if
        #end if
    #end if
    return redirect(reverse('domicilios:api_index_pedido'))

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

@csrf_exempt
def searchTablaItems(request):
    print 'usuario q llega %d'%request.user.id,request.GET.get('start'),request.GET.get('columns[1][search][value]','')
    length=request.GET.get('length','0')
    columnas = ['nombre','descripcion']
    num_columno = request.GET.get('order[0][column]','0')
    order = request.GET.get('order[0][dir]',0)
    busqueda = request.GET.get('columns[1][search][value]','')
    start  = int(request.GET.get('start',0))
    search = request.GET.get('search[value]',False)
    cursor = connection.cursor()
    m = 'select tabla_items(%d,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer)'%(request.user.id,busqueda,order,start,length)
    cursor.execute(m)
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def

@csrf_exempt
def despacharPedidoTablaAjax(request):
    length=request.GET.get('length','0')
    columnas = ['nombre','descripcion']
    num_columno = request.GET.get('order[0][column]','0')
    order = request.GET.get('order[0][dir]',0)
    busqueda = request.GET.get('columns[1][search][value]','')
    start  = request.GET.get('start',0)
    search = request.GET.get('search[value]',False)
    cursor = connection.cursor()
    cursor.execute('select tabla_pedidos_despacho(%d,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer)'%(request.user.id,busqueda,order,start,length))
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def


@supervisor_required
@administrador_required
def despacharPedidoAjax(request):
    return render(request, 'api/pedidos/despacharpedido.html')
#end def

@csrf_exempt
def updatePedidoService(request):
    id_pedido = request.POST.get('id_ped',False)
    if id_pedido :
        Pedido.objects.filter(id=int(id_pedido)).update(despachado=True)
        return HttpResponse("true",content_type="application/json")
    #end if
    return HttpResponse("false",content_type="application/json")
#end def

@csrf_exempt
def updatePedidoEntregaService(request):
    id_pedido = request.POST.get('id_ped',False)
    if id_pedido :
        pedido = Pedido.objects.filter(id=int(id_pedido)).first()
        if pedido :
            if pedido.despachado :
                Pedido.objects.filter(id=int(id_pedido)).update(entregado=True)
                return HttpResponse("true",content_type="application/json")
            #end if
        #end if
    #end if
    return HttpResponse("false",content_type="application/json")
#end def

@csrf_exempt
def updatePedidoEntregaMotService(request):
    id_pedido = request.POST.get('id_ped',False)
    if id_pedido :
        pedido = Pedido.objects.filter(id=int(id_pedido)).first()
        if pedido :
            Pedido.objects.filter(id=int(id_pedido)).update(entregado=True)
            return HttpResponse("true",content_type="application/json")
        #end if
    #end if
    return HttpResponse("false",content_type="application/json")
#end def

def foto(request):
    return render(request,'api/pedidos/foto.html')
#end def


@csrf_exempt
def wsPedidoEmpresa(request):
    #print   (request.body.decode('utf-8')),request.body, 'jajajja' if request.body else 'nooo'
    #print 'correcto' if request.body.decode('utf-8') != 'undefined=' else 'mala'
    #print request.body.decode('utf-8')
    #print json.loads((request.body.decode('utf-8')))
    """
    for x in json.loads((request.body.decode('utf-8'))):
        print x
        print x['total_pedido']
        print x['tienda']['identificador']
        print x['cliente']
        print x['descripcion_pedido']
    """
    #end for
    print request.body.decode('utf-8')
    cursor = connection.cursor()
    cursor.execute('select ws_add_pedido_service(\'%s\'::json)'%request.body.decode('utf-8'))
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def

@csrf_exempt
def wsNotificacion(request):
    cursor = connection.cursor()
    cursor.execute('select ws_notif_pedidos(\'%s\'::integer)'%request.user.id)
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def
