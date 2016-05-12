from django.conf.urls import patterns, url

urlpatterns = patterns('domicilios.views.users.cliente',
	url(r'^add/$', 'addCliente', name="add_cliente"),
	url(r'^info/(?P<cliente_id>[0-9]+)/cliente/$', 'infoCliente', name="info_cliente"),
	url(r'^edit/(?P<cliente_id>[0-9]+)/cliente/$', 'editCliente', name="edit_cliente"),
	url(r'^$', 'index', name="index_cliente"),
	url(r'^search/$','clienteSearch', name="cliente_search"),
	url(r'^search/results/$','clienteResults', name="cliente_results"),
)
