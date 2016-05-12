from django.conf.urls import patterns, url, include

urlpatterns = patterns('domicilios.views.api.users.empleado',
	url(r'^add/$', 'addEmpleado', name="api_add_empleado"),
	url(r'^change/(?P<empleado_id>[0-9]+)/status/$', 'status',name="api_status"),
	url(r'^edit/(?P<empleado_id>[0-9]+)/info/$', 'editEmpleado',name="api_edit_info"),
	url(r'^info/(?P<empleado_id>[0-9]+)/empleado/$', 'infoEmpleado', name="api_info_empleado"),
	url(r'^passchange/(?P<empleado_id>[0-9]+)/empleado/$', 'passChangeEmpleado', name="api_passChange_empleado"),
	url(r'^search/$', 'empleadoSearch', name="api_empleado_search"),
	url(r'^search/results/$', 'empleadoResults', name="api_empleado_results"),
	url(r'^$', 'index', name="api_index_empleado"),
)

urlpatterns += patterns('domicilios.views.api.users.empleado',
	url(r'^search/empleado/$', 'searchEmpleadoTabla', name="searchEmpleadoTabla"),

)