from django.conf.urls import patterns, url

urlpatterns = patterns('domicilios.views.api.users.cliente',
	url(r'^add/$', 'addCliente', name="api_add_cliente"),
	url(r'^info/(?P<cliente_id>[0-9]+)/cliente/$', 'infoCliente', name="api_info_cliente"),
	url(r'^edit/(?P<cliente_id>[0-9]+)/cliente/$', 'editCliente', name="api_edit_cliente"),
	url(r'^$', 'index', name="api_index_cliente"),
	url(r'^search/$','clienteSearch', name="api_cliente_search"),
	url(r'^search/results/$','clienteResults', name="api_cliente_results"),
)


#servicio de tabla de cliente
urlpatterns+=patterns('domicilios.views.api.users.cliente',
	url(r'^search/cliente/$', 'searchCliente', name="searchCliente"),
)