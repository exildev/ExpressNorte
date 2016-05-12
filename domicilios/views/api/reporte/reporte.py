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
from domicilios.forms.users.empresaForm import *
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib import colors
import json as simplejson
from datetime import date
import csv

@administrador_required
def index(request):
	return render(request,'api/reporte/index.html',{})
#end def

@administrador_required
def pedidos(request):
	return render(request,'api/reporte/pedidos.html')
#end def

@administrador_required
def empleados(request):
	empresa = Empresa.objects.filter(empleado__id=request.user.id).first()
	e= None
	if empresa :
		e = Empleado.objects.filter(empresa=empresa).order_by('first_name','last_name')
	#end if
	return render(request,'api/reporte/empleados.html',{'empleados':e})
#end def

@csrf_exempt
def repopedidos_ajax(request):
    length=request.GET.get('length','0')
    columnas = ['nombre','descripcion']
    num_columno = request.GET.get('order[0][column]','0')
    order = request.GET.get('order[0][dir]',0)
    busqueda = request.GET.get('columns[1][search][value]','')
    start  = request.GET.get('start',0)
    search = request.GET.get('search[value]',False)
    cursor = connection.cursor()
    cursor.execute('select reporte_pedidos(%d,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer)'%(request.user.id,busqueda,order,start,length))
    row = cursor.fetchone()
    return HttpResponse(row[0],content_type="application/json")
#end def

@administrador_required
@csrf_exempt
def ser_tab_empleado(request):
	return render(request,'api/reporte/tablaempleado.html')
#end def

@csrf_exempt
def repopedidos_ajax_empleado(request):
	id_tra = request.GET.get('id_emp','0')
	length=request.GET.get('length','0')
	columnas = ['nombre','descripcion']
	num_columno = request.GET.get('order[0][column]','0')
	order = request.GET.get('order[0][dir]',0)
	busqueda = request.GET.get('columns[1][search][value]','')
	start  = request.GET.get('start',0)
	search = request.GET.get('search[value]',False)
	cursor = connection.cursor()
	m = 'select reporte_tiempos_empleados(%s,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer,%s::integer)'%(id_tra,busqueda,order,start,length,request.user.id)
	cursor.execute(m)
	row = cursor.fetchone()
	return HttpResponse(row[0],content_type="application/json")
#end def

@administrador_required
def tipoempleado(request):
	return render(request,'api/reporte/tipoempleado.html',{'form':AddEmpresaForm()})
#end def

@csrf_exempt
def ser_tab_info_emp(request):
	id_tra_tipo = request.GET.get('id_emp_tipo','')
	id_ciudad= request.GET.get('ciudad','')
	length=request.GET.get('length','0')
	columnas = ['nombre','descripcion']
	num_columno = request.GET.get('order[0][column]','0')
	order = request.GET.get('order[0][dir]',0)
	busqueda = request.GET.get('columns[1][search][value]','')
	start  = request.GET.get('start',0)
	search = request.GET.get('search[value]',False)
	cursor = connection.cursor()
	m = 'select tabla_info_empleado(%s,\'%s\'::text,\'%s\'::text,%s::integer,%s::integer,\'%s\'::text,\'%s\'::text)'%(request.user.id,busqueda,order,start,length,id_ciudad,id_tra_tipo)
	cursor.execute(m)
	row = cursor.fetchone()
	return HttpResponse(row[0],content_type="application/json")
#end def

@csrf_exempt
def report_empleado_pdf(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment; filename=Reporte_Empleado.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer,pagesize=A4)
	#return (array_to_json(array_agg(row_to_json(row(b,res)))));
	#Header
	id_emp = request.GET.get('id','0')
	ini = request.GET.get('inicio','2015-01-01')
	fin = request.GET.get('fin','%s-%s-%s'%(date.today().year,date.today().month,date.today().day))
	#CURSOR DE LA INFO EMPLEADO
	cursor = connection.cursor()
	cursor.execute('select get_info_empleados_report(%s,\'%s\',\'%s\')'%(id_emp,ini,fin))
	#cursor.execute('select get_info_empleados_report(18,\'2016-05-04\',\'2016-05-04\')')
	row = cursor.fetchone()
	res =simplejson.loads('%s'%row[0])
	#
	if len(res) > 0 :
		trab = res[0]['f1'][0]
		c.setLineWidth(.3)
		c.setFont('Helvetica',22)
		c.drawString(30,750,trab['nom'])
		c.drawString(30,730,trab['iden'])
		c.drawString(30,710,trab['correo'])
		c.drawString(30,686,trab['tel'])
		response['Content-Disposition']='attachment; filename=Empleado %s.pdf'%trab['nom']
		"""c.setFont('Helvetica',12)
		c.drawString(30,735,'Report')"""

		c.setFont('Helvetica-Bold',12)
		c.drawString(480,750,'%s/%s/%s'%(date.today().day,date.today().month,date.today().year))
		c.line(460,747,560,747)

		emp = res[0]['f2']
		print emp
		#cuerpo de la tabla

		#Table header
		styles = getSampleStyleSheet()
		styleBH =styles["Normal"]
		styles.alingnment = TA_CENTER
		styleBH.fontSize = 10

		cliente = Paragraph('''Cliente''',styleBH)
		direccion = Paragraph('''Direccion''',styleBH)
		total = Paragraph('''Total''',styleBH)
		motorizado = Paragraph('''Motorizado''',styleBH)
		alistar = Paragraph('''Alistamiento(Min)''',styleBH)
		despacho = Paragraph('''Despacho(Min)''',styleBH)
		entrega = Paragraph('''Entrega(Min)''',styleBH)

		data = []
		data.append([cliente,direccion,total,motorizado,alistar,despacho,entrega])

		#table
		styleN = styles["BodyText"]
		styleN.alingnment= TA_CENTER
		styleN.fontSize = 7

		high = 650
		for student in emp :
			this_student =[student['cliente'][0:15],student['direccion'][0:15],student['total'],student['motori'][0:15],student['alistar'],student['despacho'],student['entrega']]
			data.append(this_student)
			high = high -18
		#end for

		width,height = A4
		table = Table(data,colWidths=[3*cm,3*cm,2*cm,3*cm,2.5*cm,2.5*cm,2.5*cm])
		table.setStyle([
			('INNERGRID',(0,0),(-1,-1),0.25,colors.black),
			('BOX',(0,0),(-1,-1),0.25,colors.black)
			,])
		table.wrapOn(c,width,height)
		table.drawOn(c,30,high)
	else :
		c.drawString(30,750,'Empleado no registrado')
	#end if
	c.showPage()#save page
	c.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response
#end def

@csrf_exempt
def report_empleado_excel(request):
	id_emp = request.GET.get('id','0')
	ini = request.GET.get('inicio','2015-01-01')
	fin = request.GET.get('fin','%s-%s-%s'%(date.today().year,date.today().month,date.today().day))
	#CURSOR DE LA INFO EMPLEADO
	cursor = connection.cursor()
	cursor.execute('select get_info_empleados_report(%s,\'%s\',\'%s\')'%(id_emp,ini,fin))
	#cursor.execute('select get_info_empleados_report(18,\'2016-05-04\',\'2016-05-04\')')
	row = cursor.fetchone()
	res =simplejson.loads('%s'%row[0])
	# Create the HttpResponse object with the appropriate CSV header.
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="Reporte Empleado.csv"'
	#
	writer = csv.writer(response)
	if len(res) > 0 :
		response['Content-Disposition'] = 'attachment; filename="Reporte Empleado.csv"'
		writer = csv.writer(response)
		#----------------------------------
		trab = res[0]['f1'][0]
		writer.writerow(['Nombre Empleado',trab['nom']])
		writer.writerow(['Identificación',trab['iden']])
		writer.writerow(['Correo',trab['correo']])
		writer.writerow(['Telefono',trab['tel']])
		#----------------------------------
		emp = res[0]['f2']
		writer.writerow(['Cliente','Direccion','Total','Motorizado','Alistamiento(Min)','Despacho(Min)','Entrega(Min)'])
		for res in emp :
			writer.writerow([res['cliente'],res['direccion'],res['total'],res['motori'],res['alistar'],res['despacho'],res['entrega']])
		#end def
		
	else:
		writer.writerow(['Trabajador no encontrado'])
	#end if
	return response
#end def