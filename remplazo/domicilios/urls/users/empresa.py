from django.conf.urls import patterns, url

urlpatterns = patterns('domicilios.views.users.empresa',
	url(r'^add/$', 'addEmpresa', name="add_empresa"),
	url(r'^info/(?P<empresa_id>[0-9]+)/empresa/$', 'infoEmpresa', name="info_empresa"),
	url(r'^edit/(?P<empresa_id>[0-9]+)/empresa/$', 'editEmpresa', name="edit_empresa"),
	url(r'^$', 'index', name="index_empresa"),
	url(r'^search/$', 'empresaSearch', name="empresa_search"),
	url(r'^search/results/$', 'empresaResults', name="empresa_results"),
	url(r'^change/(?P<empresa_id>[0-9]+)/status/$', 'status',name="status"),
)
