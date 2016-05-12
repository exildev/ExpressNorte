from django.conf.urls import patterns, include, url
from easy_pdf.views import PDFTemplateView
from domicilios.views.pedido.pedido import facturaPedido

urlpatterns = patterns('domicilios.views.pedido.pedido',
	url(r'^$', 'index', name="index_pedido"),
	url(r'add/pedido/$', 'addPedido' , name="add_pedido"),
	url(r'add/$', 'addPedidoAdmin' , name="add_pedido_admin"),
	url(r'edit/(?P<pedido_id>[0-9]+)/$', 'editPedido', name="edit_pedido"),
	url(r'(?P<pedido_id>[0-9]+)/edit/items/$', 'editPedidoItems', name="api_edit_pedido_items"),
	url(r'add/items/$', 'addItems', name="add_items"),
	url(r'edit/item/(?P<item_id>[0-9]+)/$', 'editItems', name="edit_items"),
	url(r'nuevo/item/$', 'addItemPedido', name="item_pedido"),
	url(r'add/pedido/items/$', 'pedidoItems', name="add_pedido_items"),
	url(r'item/(?P<item_id>[0-9]+)/pedido/$', 'deletePedidoItems', name="delete_pedido_items"),
	url(r'item/(?P<item_id>[0-9]+)/edit/$', 'deletePedidoItemsEdit', name="delete_pedido_items_edit"),
	url(r'total/$', 'totalPedido', name="total_pedido"),
	url(r'total/edit/$', 'totalPedidoEdit', name="total_pedido_edit"),
	url(r'asignar/$', 'asignarMotorizado', name="asignar"),
	url(r'(?P<pedido_id>[a-zA-Z0-9]+)/asignar/motorizado/$','chooseMotorizado',name="choose"),
	url(r'finalizar/$', 'finalizarPedido', name="finalizar_pedido"),
	url(r'search/$', 'pedidoSearch', name="pedido_search"),
	url(r'search/results/$', 'pedidoResults', name="pedido_results"),
	url(r'(?P<pedido_id>[0-9]+)/info/$', 'infoPedido', name="info_pedido"),
	url(r'asignados/$', 'misPedidos', name="mis_pedidos"),
	url(r'list/items/$', 'listItems', name="list_items"),
	url(r'list/items/results/$', 'listItemsResults', name="list_items_results"),
	url(r'factura/(?P<pedido_id>[a-zA-Z0-9-]+)$', facturaPedido.as_view(), name="factura"),
	url(r'certificado/$', 'pedidoCertificado', name="pedido_certificado"),
	url(r'comprobar/(?P<pedido_id>\w+)/$', 'comprobar_pedido', name="comprobar_pedido"),
	url(r'item/delete/(?P<item_id>[0-9]+)/$','deleteItems', name="delete_items"),

)

