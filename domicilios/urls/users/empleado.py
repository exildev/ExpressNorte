from django.conf.urls import patterns, url, include

urlpatterns = patterns('domicilios.views.users.empleado',
	url(r'^add/$', 'addEmpleado', name="add_empleado"),
	url(r'^change/(?P<empleado_id>[0-9]+)/status/$', 'status',name="status"),
	url(r'^edit/(?P<empleado_id>[0-9]+)/info/$', 'editEmpleado',name="edit_info"),
	url(r'^info/(?P<empleado_id>[0-9]+)/empleado/$', 'infoEmpleado', name="info_empleado"),
	url(r'^passchange/(?P<empleado_id>[0-9]+)/empleado/$', 'passChangeEmpleado', name="passChange_empleado"),
	url(r'^search/$', 'empleadoSearch', name="empleado_search"),
	url(r'^search/results/$', 'empleadoResults', name="empleado_results"),
	url(r'^$', 'index', name="index_empleado"),
)
