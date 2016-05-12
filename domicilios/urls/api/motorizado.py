from django.conf.urls import patterns, include, url

urlpatterns = patterns('domicilios.views.api.motorizado.motorizado',
	url(r'^add/$', 'AddMotorizado', name="api_add_motorizado"),
	url(r'^moto/add/$', 'addMoto', name="api_add_moto"),
	url(r'^moto/asignar/$', 'asignarMoto', name="api_asignar_moto"),
	url(r'^moto/(?P<moto_id>[0-9]+)/details/$','infoMoto', name="api_info_moto"),
	url(r'^moto/(?P<moto_id>[0-9]+)/edit/$','editMoto', name="api_edit_moto"),
	url(r'^$', 'index', name="api_index_motorizado"),
	url(r'^search/$','motoSearch', name="api_moto_search"),
	url(r'^search/results/$','motoResults', name="api_moto_results"),
	url(r'^list/$', 'viewMotorizado', name="api_view_motorizado"),
	url(r'^results/$', 'motorizadoResults', name="api_motorizado_results"),
	url(r'^(?P<motorizado_id>[0-9]+)/edit/$', 'editMotorizado', name="api_edit_motorizado"),
	url(r'^delete/(?P<moto_id>[0-9]+)/$','deleteMoto',name="api_delete_moto"),
)

# tabla ajax de las motos
urlpatterns += patterns('domicilios.views.api.motorizado.motorizado',
	url(r'^search/moto/$','searchMoto', name="ajax_search_moto"),
	url(r'^search/motorizado/$','searchMotorizado', name="ajax_search_motorizado"),
	url(r'^search/motorizado/pedidos/$','searchMotorizadoPedidos', name="ajax_search_motorizadopeds"),
)

# tabla ajax de llos reportes
urlpatterns += patterns('domicilios.views.api.motorizado.motorizado',
	url(r'^reportes/$','reportes', name="reportes"),
	url(r'^search/reporte/$','searchreporte',name="searchreporte"),
)


