from django.conf.urls import patterns, include, url

urlpatterns = patterns('domicilios.views.api.reporte.reporte',
	url(r'^$', 'index', name="index_reporte"),
	url(r'^pedidos/$', 'pedidos', name="pedidos_reporte"),
	url(r'^empleados/$', 'empleados', name="empleados_reporte"),
)

#servicios de tablas
urlpatterns += patterns('domicilios.views.api.reporte.reporte',
	url(r'^servi/pedidos/$', 'repopedidos_ajax', name="repopedidos_ajax"),#retorna la tabla de tiempos de entregas de productos
	url(r'^servi/pedidos/empleado/$', 'repopedidos_ajax_empleado', name="repopedidos_ajax_empleado"),#retorna la tabla de tiempos de entregas de productos
	url(r'^servi/tabla/empleado/$','ser_tab_empleado',name="ser_tab_empleado"),#mostrar tabla con la informacion de entrega del empleado
)

#Generar la informacion de tipo de empleado, mostrar lo concerniente a un periodo de sus actividades.
urlpatterns += patterns('domicilios.views.api.reporte.reporte',
	url(r'^tipo/empleado/$', 'tipoempleado', name="tipoempleado"),#retorna la tabla de tiempos de entregas de productos
	url(r'^servi/tabla/info/empleados/$','ser_tab_info_emp',name='ser_tab_info_emp'),
	url(r'^report/empleado/pdf/$','report_empleado_pdf',name='report_empleado_pdf'),
	url(r'^report/empleado/excel/$','report_empleado_excel',name='report_empleado_excel'),
)
