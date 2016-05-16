from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from domicilios.forms.motorizado.motorizadoForm import *
from domicilios.decorators import *
from domicilios.templatetags.moto_notifications import has_exprired
from domicilios.models.motorizado import *
from domicilios.models.pedido import *
from django.db.models import Q

@supervisor_required
def AddMotorizado(request):
    motosC = Moto.objects.filter(motorizado__moto__isnull=True).count()
    empleadosC = Empleado.objects.filter(cargo='MOTORIZADO').filter(motorizado__empleado__isnull=True).count()
    if motosC > 0:
        return redirect(reverse('domicilios:asignar_moto'))
    else:
        if empleadosC > 0:
            if request.method == 'POST':
                formMoto = AddMotoForm(request.POST, instance=Moto())
                formSoat = AddSoatForm(request.POST, instance=Soat())
                formTecno = AddTecnoForm(request.POST, instance=Tecno())
                formMotorizado = AddMotorizadoForm(request.POST, instance=Motorizado())
                if formSoat.is_valid() and formTecno.is_valid() and formMoto.is_valid() and formMotorizado.is_valid():
                    new_soat = formSoat.save()
                    new_tecno = formTecno.save()
                    new_moto = formMoto.save(commit=False)
                    new_moto.tecno = new_tecno
                    new_moto.soat = new_soat
                    new_moto.save()
                    new_motorizado = formMotorizado.save(commit=False)
                    new_motorizado.moto = new_moto
                    new_motorizado.save()
                    mensaje = {'tipo':'success','texto':"Se a registrado un motorizado correctamente"}
                    return render(request, 'motorizado/index.html', {'mensaje':mensaje})
            else:
                formMoto = AddMotoForm(instance=Moto())
                formSoat = AddSoatForm(instance=Soat())
                formTecno = AddTecnoForm(instance=Tecno())
                formMotorizado = AddMotorizadoForm(instance=Motorizado())

            return render(request, 'motorizado/addMotorizado.html', {'formSoat': formSoat, 'formTecno': formTecno, 'formMoto': formMoto, 'formMotorizado': formMotorizado})
        else:
            return render(request,'motorizado/addMotorizado.html',{'mensaje2':'No hay empleados disponibles para asignarles una moto'})

@motorizado_required
def viewMotorizado(request):
    return render(request,'motorizado/motorizado.html')

@motorizado_required
def editMotorizado(request,motorizado_id):
    motorizado = get_object_or_404(Motorizado, pk=motorizado_id)
    if request.method == 'POST':
        formMotorizado = editMotorizadoForm(request.POST, instance=motorizado)
        if formMotorizado.is_valid():
            formMotorizado.save()
            motorizados = Motorizado.objects.all()
            mensaje = {'tipo':'success','texto':"Se a editado un motorizado correctamente"}
            return render(request, 'motorizado/motorizado.html', {'mensaje':mensaje,'motorizados':motorizados})
    else:
        formMotorizado = editMotorizadoForm(instance=motorizado)
    return render(request,'motorizado/editMotorizado.html',{'form':formMotorizado})

@supervisor_required
def addMoto(request):
    if request.method == 'POST':
        formMoto = AddMotoForm(request.POST, instance=Moto())
        formSoat = AddSoatForm(request.POST, instance=Soat())
        formTecno = AddTecnoForm(request.POST, instance=Tecno())
        if formSoat.is_valid() and formTecno.is_valid() and formMoto.is_valid():
            new_soat = formSoat.save()
            new_tecno = formTecno.save()
            new_moto = formMoto.save(commit=False)
            new_moto.tecno = new_tecno
            new_moto.soat = new_soat
            new_moto.save()
            mensaje = {'tipo':'success','texto':"Se a registrado una moto correctamente"}
            return render(request, 'motorizado/index.html', {'mensaje':mensaje, 'formSoat': formSoat, 'formTecno': formTecno, 'formMoto': formMoto})
    else:
        formMoto = AddMotoForm(instance=Moto())
        formSoat = AddSoatForm(instance=Soat())
        formTecno = AddTecnoForm(instance=Tecno())

    return render(request, 'motorizado/addMoto.html', {'formSoat': formSoat, 'formTecno': formTecno, 'formMoto': formMoto})

@supervisor_required
def editMoto(request, moto_id):
    moto = get_object_or_404(Moto, pk=moto_id)
    soat = Soat.objects.get(numeroS=moto.soat)
    tecno = Tecno.objects.get(numeroT=moto.tecno)
    if request.method == 'POST':
        formMoto = AddMotoForm(request.POST, instance=moto)
        formSoat = AddSoatForm(request.POST, instance=soat)
        formTecno = AddTecnoForm(request.POST, instance=tecno)
        if formSoat.is_valid() and formTecno.is_valid() and formMoto.is_valid():
            new_soat = formSoat.save()
            new_tecno = formTecno.save()
            new_moto = formMoto.save(commit=False)
            new_moto.tecno = new_tecno
            new_moto.soat = new_soat
            new_moto.save()
            mensaje = {'tipo':'positive','texto':"Se a editado una moto correctamente"}
            return render(request, 'motorizado/index.html', {'mensaje':mensaje})
    else:
        formMoto = AddMotoForm(instance=moto)
        formSoat = AddSoatForm(instance=soat)
        formTecno = AddTecnoForm(instance=tecno)

    return render(request, 'motorizado/editMoto.html', {'formSoat': formSoat, 'formTecno': formTecno, 'formMoto': formMoto})

@administrador_required
def infoMoto(request,moto_id):
    moto = get_object_or_404(Moto, pk=moto_id)
    soat = Soat.objects.get( numeroS = moto.soat)
    tecno = Tecno.objects.get(numeroT = moto.tecno)
    return render(request,'motorizado/infoMoto.html',{'moto':moto, 'soat':soat,'tecno':tecno})

def deleteMoto(request,moto_id):
    moto = get_object_or_404(Moto,pk=moto_id).delete()
    return redirect(reverse('domicilios:moto_search'))

@supervisor_required
def asignarMoto(request):
    empleadosC = Empleado.objects.filter(cargo='MOTORIZADO').filter(motorizado__empleado__isnull=True).count()
    motosC = Moto.objects.filter(motorizado__moto__isnull=True).count()

    if empleadosC > 0:
        if motosC > 0:
            if request.method == 'POST':
                form = AsignarMotoForm(request.POST)
                if form.is_valid():
                    form.save()
                    mensaje = {'tipo':'success','texto':"Se a asignado una moto correctamente"}
                    return render(request, 'motorizado/index.html', {'mensaje':mensaje})
            else:
                form = AsignarMotoForm()
            return render(request,'motorizado/asignarMoto.html',{'form':form})
        else:
            error = "No hay motos disponibles para ser asignadas"
        return render(request,'motorizado/asignarMoto.html',{'error':error})
    else:
        error = "No hay empleados disponibles para ser asignados"
    return render(request,'motorizado/asignarMoto.html',{'error':error})

@motorizado_required
def notificacionesMoto(request):
    h = has_exprired("get")
    return render(request,'motorizado/notificaciones.html', h)

@supervisor_required
def index(request):
    return render(request,'motorizado/index.html')

def motoSearch(request):
    return render(request,'motorizado/motoSearch.html')

@motorizado_required
def motoResults(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text != '':
            motos = Moto.objects.filter(placa__icontains=search_text)
            return render(request,'motorizado/ajax_search.html',{'motos':motos})
        else:
            motos = Moto.objects.all()
            return render(request,'motorizado/ajax_search.html',{'motos':motos})
    return render(request,'motorizado/ajax_search.html')

def motorizadoResults(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text != '':
            motorizados = Motorizado.objects.filter(
                Q(empleado__last_name__icontains=search_text) | Q(empleado__identificacion__icontains=search_text))
            return render(request,'motorizado/ajax_motorizado.html',{'motorizados':motorizados})
        else:
            motorizados = Motorizado.objects.all()
            return render(request,'motorizado/ajax_motorizado.html',{'motorizados':motorizados})
    return render(request,'motorizado/ajax_motorizado.html')

from datetime import date, timedelta

def reporte(request):
    if request.method == 'POST':
        form = reporteForm(request.POST)
        if 'motorizado' in request.POST:
            return redirect('/motorizado/reporte1/'+request.POST['ciudad']+'/'+request.POST['fecha_inicio']+'/'+request.POST['fecha_final'])
        else:
            return redirect('/motorizado/reporte/'+request.POST['ciudad']+'/'+request.POST['fecha_inicio']+'/'+request.POST['fecha_final'])
    form = reporteForm()
    return render(request,'motorizado/reporte.html',{'form':form})


def reporteMoto(request,ciudad,fi,ff):
    if request.method == 'POST':
        return redirect('/motorizado/reporte2/'+request.POST['moto']+'/'+fi+'/'+ff)
    Moto = Motorizado.objects.filter(Q(empleado__ciudad__icontains=ciudad))
    return render(request,'motorizado/reporteMoto.html',{'Moto':Moto})

from easy_pdf.views import PDFTemplateView

class reporte1(PDFTemplateView):
    template_name = "motorizado/reporte1.html"

    def get_context_data(self, ciudad, fi, ff, **kwargs):

        pedidos = Pedido.objects.filter(Q(motorizado__ciudad__icontains=ciudad),Q(fecha_pedido__range=[fi,ff]))
        tiempos= Tiempo.objects.filter(Q(pedido__icontains=pedidos))
        return super(reporte1, self).get_context_data(
            pagesize="A5",
            title="Pedido",
            ciudad=ciudad, pedidos=pedidos, tiempos=tiempos,
            **kwargs
        )

class reporte2(PDFTemplateView):
    template_name = "motorizado/reporte2.html"

    def get_context_data(self, moto, fi, ff, **kwargs):
        Moto=Empleado.objects.get(identificacion=moto)
        pedidos = Pedido.objects.filter(Q(motorizado__identificacion__icontains=moto),Q(fecha_pedido__range=[fi,ff]))
        return super(reporte2, self).get_context_data(
            pagesize="A4",
            title="Pedido",
            pedidos=pedidos, Moto=Moto,
            **kwargs
        )
    #end def
#end class


