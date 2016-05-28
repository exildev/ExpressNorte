from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.urlresolvers import reverse
from domicilios.forms.motorizado.motorizadoForm import *
from domicilios.forms.users.empresaForm import *
from domicilios.decorators import *
from domicilios.models.users import Empresa, Empleado
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from datetime import date

def userEmpresa(request, num):
    user = Empleado.objects.get(username=request.user)
    empresa = Empresa.objects.get(first_name=user.empresa)
    if num == 1:
        return user
    if num == 2:
        return empresa

@supervisor_required
def index(request):
    return render(request,'api/motorizado/index.html')

@supervisor_required
def addMoto(request):
    if request.method == 'POST':
        formMoto = AddMotoApiForm(request.POST, instance=Moto())
        formSoat = AddSoatForm(request.POST, instance=Soat())
        formTecno = AddTecnoForm(request.POST, instance=Tecno())
        if formSoat.is_valid() and formTecno.is_valid() and formMoto.is_valid():
            new_soat = formSoat.save()
            new_tecno = formTecno.save()
            new_moto = formMoto.save(commit=False)
            new_moto.tecno = new_tecno
            new_moto.soat = new_soat
            new_moto.empresaM = userEmpresa(request,2)
            new_moto.save()
            mensaje = {'tipo':'success','texto':"Se a registrado una moto correctamente"}
            return render(request, 'api/motorizado/index.html', {'mensaje':mensaje})
    else:
        formMoto = AddMotoApiForm(instance=Moto())
        formSoat = AddSoatForm(instance=Soat())
        formTecno = AddTecnoForm(instance=Tecno())

    return render(request, 'api/motorizado/addMoto.html', {'formSoat': formSoat, 'formTecno': formTecno, 'formMoto': formMoto})

def deleteMoto(request,moto_id):
    moto = get_object_or_404(Moto,pk=moto_id).delete()
    return redirect(reverse('domicilios:api_moto_search'))

def motoSearch(request):
    return render(request,'api/motorizado/motoSearch.html')

def reportes(request):
    return render(request,'api/motorizado/reportemotorizados.html',{'form':AddEmpresaForm()})
#end def

def motoResults(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text != '':
            motos = Moto.objects.filter(placa__icontains=search_text)
            return render(request,'api/motorizado/ajax_search.html',{'motos':motos})
        else:
            empresa = userEmpresa(request,2)
            motos = Moto.objects.filter(empresaM=empresa)
            return render(request,'api/motorizado/ajax_search.html',{'motos':motos})
    return render(request,'api/motorizado/ajax_search.html')

@administrador_required
def infoMoto(request,moto_id):
    moto = get_object_or_404(Moto, pk=moto_id)
    soat = Soat.objects.get( numeroS = moto.soat)
    tecno = Tecno.objects.get(numeroT = moto.tecno)
    return render(request,'api/motorizado/infoMoto.html',{'moto':moto, 'soat':soat,'tecno':tecno})

@supervisor_required
def editMoto(request, moto_id):
    moto = get_object_or_404(Moto, pk=moto_id)
    soat = Soat.objects.get(numeroS=moto.soat)
    tecno = Tecno.objects.get(numeroT=moto.tecno)
    if request.method == 'POST':
        formMoto = AddMotoApiForm(request.POST, instance=moto)
        formSoat = AddSoatForm(request.POST, instance=soat)
        formTecno = AddTecnoForm(request.POST, instance=tecno)
        if formSoat.is_valid() and formTecno.is_valid() and formMoto.is_valid():
            new_soat = formSoat.save()
            new_tecno = formTecno.save()
            new_moto = formMoto.save(commit=False)
            new_moto.tecno = new_tecno
            new_moto.soat = new_soat
            new_moto.empresaM = userEmpresa(request,2)
            new_moto.save()
            mensaje = {'tipo':'positive','texto':"Se a editado una moto correctamente"}
            return render(request,'api/motorizado/editMoto.html', {'mensaje':mensaje,'formSoat': formSoat, 'formTecno': formTecno, 'formMoto': formMoto})
    else:
        formMoto = AddMotoForm(instance=moto)
        formSoat = AddSoatForm(instance=soat)
        formTecno = AddTecnoForm(instance=tecno)

    return render(request,'api/motorizado/editMoto.html', {'formSoat': formSoat, 'formTecno': formTecno, 'formMoto': formMoto})

@supervisor_required
def asignarMoto(request):
    empresa = userEmpresa(request,2)
    empleadosC = Empleado.objects.filter(cargo='MOTORIZADO').filter(empresa=empresa,motorizado__empleado__isnull=True)
    motosC = Moto.objects.filter(empresaM=empresa).filter(motorizado__moto__isnull=True,estado=True)
    print 'aqui',len(empleadosC)
    if empleadosC :
        if motosC :
            if request.method == 'POST':
                form = AsignarMotoApiForm(request.POST)
                if form.is_valid():
                    form.save()
                    mensaje = {'tipo':'success','texto':"Se a asignado una moto correctamente"}
                    return render(request, 'api/motorizado/asignarMoto.html', {'mensaje':mensaje,'form':form})
                else:
                    print 'la vaina no es valida',form.errors
                    form.fields["moto"].queryset= motosC
                    form.fields["empleado"].queryset= empleadosC
                    return render(request, 'api/motorizado/asignarMoto.html', {'form':form})
                #end if
            else:
                form = AsignarMotoApiForm()
                form.fields["moto"].queryset= motosC
                form.fields["empleado"].queryset= empleadosC
            return render(request,'api/motorizado/asignarMoto.html',{'form':form})
        else:
            error = "No hay motos disponibles para ser asignadas"
        return render(request,'api/motorizado/asignarMoto.html',{'error':error})
    else:
        error = "No hay empleados disponibles para ser asignados"
    return render(request,'api/motorizado/asignarMoto.html',{'error':error})

@supervisor_required
def AddMotorizado(request):
    empresa = userEmpresa(request,2)
    motosC = Moto.objects.filter(empresaM=empresa).filter(motorizado__moto__isnull=True).count()
    empleadosC = Empleado.objects.filter(cargo='MOTORIZADO').filter(empresa=empresa,motorizado__empleado__isnull=True).count()
    if motosC > 0:
        return redirect(reverse('domicilios:api_asignar_moto'))
    else:
        if empleadosC > 0:
            if request.method == 'POST':
                formMoto = AddMotoApiForm(request.POST, instance=Moto())
                formSoat = AddSoatForm(request.POST, instance=Soat())
                formTecno = AddTecnoForm(request.POST, instance=Tecno())
                formMotorizado = AddMotorizadoForm(request.POST, instance=Motorizado())
                if formSoat.is_valid() and formTecno.is_valid() and formMoto.is_valid() and formMotorizado.is_valid():
                    new_soat = formSoat.save()
                    new_tecno = formTecno.save()
                    new_moto = formMoto.save(commit=False)
                    new_moto.tecno = new_tecno
                    new_moto.soat = new_soat
                    new_moto.empresaM = empresa
                    new_moto.save()
                    new_motorizado = formMotorizado.save(commit=False)
                    new_motorizado.moto = new_moto
                    new_motorizado.save()
                    mensaje = {'tipo':'success','texto':"Se a registrado un motorizado correctamente"}
                    return render(request, 'api/motorizado/addMotorizado.html', {'mensaje':mensaje,'formSoat': formSoat, 'formTecno': formTecno, 'formMoto': formMoto, 'formMotorizado': formMotorizado})
            else:
                formMoto = AddMotoApiForm(instance=Moto())
                formSoat = AddSoatForm(instance=Soat())
                formTecno = AddTecnoForm(instance=Tecno())
                formMotorizado = AddMotorizadoApiForm(instance=Motorizado())
                formMotorizado.fields["empleado"].queryset= empleadosC = Empleado.objects.filter(cargo='MOTORIZADO').filter(empresa=empresa,motorizado__empleado__isnull=True)

            return render(request, 'api/motorizado/addMotorizado.html', {'formSoat': formSoat, 'formTecno': formTecno, 'formMoto': formMoto, 'formMotorizado': formMotorizado})
        else:
            return render(request,'api/motorizado/addMotorizado.html',{'error':'No hay empleados disponibles para asignarles una moto'})


def viewMotorizado(request):
    return render(request,'api/motorizado/motorizado.html')

def editMotorizado(request,motorizado_id):
    motorizado = get_object_or_404(Motorizado, pk=motorizado_id)
    if request.method == 'POST':
        formMotorizado = editMotorizadoForm(request.POST, instance=motorizado)
        if formMotorizado.is_valid():
            formMotorizado.save()
            motorizados = Motorizado.objects.all()
            mensaje = {'tipo':'success','texto':"Se a editado un motorizado correctamente"}
            return render(request, 'api/motorizado/motorizado.html', {'mensaje':mensaje,'motorizados':motorizados})
    else:
        emp = Empresa.objects.filter(empleado__id=request.user.id).values('first_name').first()
        emp = emp['first_name'] if emp else False
        formMotorizado = editMotorizadoForm(instance=motorizado)
    return render(request,'api/motorizado/editMotorizado.html',{'form':formMotorizado,'empresa':emp,'motorizado':motorizado_id})

def motorizadoResults(request):
    empresa = userEmpresa(request,2)
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text != '':
            motorizados = Motorizado.objects.filter(empresa=empresa).filter(
                Q(empleado__last_name__icontains=search_text) | Q(empleado__identificacion__icontains=search_text))
            return render(request,'api/motorizado/ajax_motorizado.html',{'motorizados':motorizados})
        else:
            motorizados = Motorizado.objects.all()
            return render(request,'api/motorizado/ajax_motorizado.html',{'motorizados':motorizados})
    return render(request,'api/motorizado/ajax_motorizado.html')

@csrf_exempt
def searchMoto(request):
    length=request.GET.get('length','0')
    columnas = ['nombre','descripcion']
    num_columno = request.GET.get('order[0][column]','0')
    order = request.GET.get('order[0][dir]',0)
    busqueda = request.GET.get('columns[1][search][value]','')
    start  = request.GET.get('start',0)
    search = request.GET.get('search[value]',False)
    cursor = connection.cursor()
    cursor.execute('select tabla_moto(%d,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer)'%(request.user.id,busqueda,order,start,length))
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def

@csrf_exempt
def searchMotorizado(request):
    length=request.GET.get('length','0')
    columnas = ['nombre','descripcion']
    num_columno = request.GET.get('order[0][column]','0')
    order = request.GET.get('order[0][dir]',0)
    busqueda = request.GET.get('columns[1][search][value]','')
    start  = request.GET.get('start',0)
    search = request.GET.get('search[value]',False)
    cursor = connection.cursor()
    cursor.execute('select tabla_motorizado(%d,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer)'%(request.user.id,busqueda,order,start,length))
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def

@csrf_exempt
def searchMotorizadoPedidos(request):
    length=request.GET.get('length','0')
    columnas = ['nombre','descripcion']
    num_columno = request.GET.get('order[0][column]','0')
    order = request.GET.get('order[0][dir]',0)
    busqueda = request.GET.get('columns[1][search][value]','')
    start  = request.GET.get('start',0)
    search = request.GET.get('search[value]','')
    cursor = connection.cursor()
    cursor.execute('select tabla_pedidos_motorizado(%d,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer)'%(request.user.id,search,order,start,length))
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def

@csrf_exempt
def searchreporte(request):
    inicio= request.GET.get('ini',date.today())
    fin = request.GET.get('fin','2005-01-01')
    length=request.GET.get('length','0')
    columnas = ['nombre','descripcion']
    num_columno = request.GET.get('order[0][column]','0')
    order = request.GET.get('order[0][dir]',0)
    busqueda = request.GET.get('columns[1][search][value]','')
    start  = request.GET.get('start',0)
    search = request.GET.get('search[value]','')
    cursor = connection.cursor()
    cursor.execute('select reporte_tiempos(%d,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer)'%(request.user.id,search,order,start,length))
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def


def rastre_motorizado(request):
    emp = Empresa.objects.filter(empleado__id=request.user.id).values('first_name').first()
    emp = emp['first_name'] if emp else False
    return render(request,'api/motorizado/rastreo.html',{'empresa':emp})
#en def


@csrf_exempt
def listar_motorizado_rastreo(request):
    print request.POST
    busq = request.POST.get('busq','')
    start = request.POST.get('start','0')
    pag = request.POST.get('pag','10')
    cursor = connection.cursor()
    #cursor.execute('select listar_motorizados_rastreo(%d,\'jajajaj\'::text,%s::integer,%s::integer)'%(request.user.id,busq,start,pag))
    cursor.execute('select ws_rastreo_lis_motorizado(5,\'jajajaj\'::text,1,10)')
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def
