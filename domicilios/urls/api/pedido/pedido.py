from django.conf.urls import patterns, include, url
from domicilios.views.api.pedido.pedido import facturaPedido

urlpatterns = patterns('domicilios.views.api.pedido.pedido',
	url(r'^$', 'index', name="api_index_pedido"),
	url(r'add/$', 'addPedido' , name="api_add_pedido"),
	url(r'edit/(?P<pedido_id>[0-9]+)/$', 'editPedido', name="api_edit_pedido"),
	url(r'(?P<pedido_id>[0-9]+)/edit/items/$', 'editPedidoItems', name="api_edit_pedido_items"),
	url(r'item/(?P<item_id>[0-9]+)/edit/$', 'deletePedidoItemsEdit', name="api_delete_pedido_items_edit"),
	url(r'add/pedido/$', 'addPedidoAdmin' , name="api_add_pedido_admin"),
	url(r'add/items/$', 'addItems', name="api_add_items"),
	url(r'(?P<pedido_id>[0-9]+)/edit/items/$', 'editPedidoItems', name="api_edit_pedido_items"),
	url(r'nuevo/item/$', 'addItemPedido', name="api_item_pedido"),
	url(r'add/pedido/items/$', 'pedidoItems', name="api_add_pedido_items"),
	url(r'item/(?P<item_id>[0-9]+)/pedido/$', 'deletePedidoItems', name="api_delete_pedido_items"),
	url(r'total/$', 'totalPedido', name="api_total_pedido"),
	url(r'total/edit/$', 'totalPedidoEdit', name="api_total_pedido_edit"),
	url(r'asignar/$', 'asignarMotorizado', name="api_asignar"),
	url(r'(?P<pedido_id>[a-zA-Z0-9-]+)/asignar/motorizado/$','chooseMotorizado',name="api_choose"),
	url(r'finalizar/$', 'finalizarPedido', name="api_finalizar_pedido"),
	url(r'search/$', 'pedidoSearch', name="api_pedido_search"),
	url(r'search/results/$', 'pedidoResults', name="api_pedido_results"),
	url(r'(?P<pedido_id>[0-9]+)/info/$', 'infoPedido', name="api_info_pedido"),
	url(r'asignados/$', 'misPedidos', name="api_mis_pedidos"),
	url(r'list/items/$', 'listItems', name="api_list_items"),
	url(r'list/items/results/$', 'listItemsResults', name="api_list_items_results"),
	url(r'edit/item/(?P<item_id>[0-9]+)/$', 'editItems', name="api_edit_items"),
	url(r'certificado/$', 'pedidoCertificado', name="api_pedido_certificado"),
	url(r'factura/(?P<pedido_id>[a-zA-Z0-9-]+)$', facturaPedido.as_view(), name="api_factura"),
)

#Tabla de pedidos y servicios
urlpatterns +=patterns('domicilios.views.api.pedido.pedido',
	url(r'search/pedidos/$','searchTablaPedidos',name="searchTablaPedidos"),
	url(r'search/items/$','searchTablaItems',name="searchTablaItems"),
	url(r'despachar/$','despacharPedidoAjax',name="despacharPedidoAjax"),
	url(r'search/tabladespacho/$','despacharPedidoTablaAjax',name="despacharPedidoTablaAjax"),
	url(r'update/pedido/$','updatePedidoService',name="updatePedidoService"),
	url(r'update/entrega/$','updatePedidoEntregaService',name="updatePedidoEntregaService"),
	url(r'update/entrega/motorizado/$','updatePedidoEntregaMotService',name="updatePedidoEntregaMotService"),
	)

# Capturar Foto
urlpatterns += patterns('domicilios.views.api.pedido.pedido',
	url(r'^foto/$','foto', name="foto"),
)

#domicilios Web
urlpatterns += patterns('domicilios.views.api.pedido.pedido',
    url(r'^ws/pedido/rest/$','wsPedidoEmpresa', name="wsPedidoEmpresa"),#Servicio que recibe los pedidos
	url(r'^ws/notificaciones/$','wsNotificacion',name="wsNotificacion"),

)
