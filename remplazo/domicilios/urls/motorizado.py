from django.conf.urls import patterns, include, url
from easy_pdf.views import PDFTemplateView
from domicilios.views.motorizado.motorizado import reporte1, reporte2

urlpatterns = patterns('domicilios.views.motorizado.motorizado',
	url(r'^add/$', 'AddMotorizado', name="add_motorizado"),
	url(r'^moto/add/$', 'addMoto', name="add_moto"),
	url(r'^moto/asignar/$', 'asignarMoto', name="asignar_moto"),
	url(r'^moto/(?P<moto_id>[0-9]+)/details/$','infoMoto', name="info_moto"),
	url(r'^moto/(?P<moto_id>[0-9]+)/edit/$','editMoto', name="edit_moto"),
	url(r'^moto/notificaciones/$', 'notificacionesMoto', name="notificaciones_moto"),
	url(r'^$', 'index', name="index_motorizado"),
	url(r'^search/$','motoSearch', name="moto_search"),
	url(r'^search/results/$','motoResults', name="moto_results"),
	url(r'^list/$', 'viewMotorizado', name="view_motorizado"),
	url(r'^results/$', 'motorizadoResults', name="motorizado_results"),
	url(r'^(?P<motorizado_id>[0-9]+)/edit/$', 'editMotorizado', name="edit_motorizado"),
	url(r'^delete/(?P<moto_id>[0-9]+)/$','deleteMoto',name="delete_moto"),
	url(r'^reporte/$','reporte',name="reporte"),
	url(r'reporte1/(?P<ciudad>[a-zA-Z0-9-]+)/(?P<fi>[a-zA-Z0-9-]+)/(?P<ff>[a-zA-Z0-9-]+)$', reporte1.as_view(), name="reporte1"),
	url(r'reporte2/(?P<moto>[a-zA-Z0-9-]+)/(?P<fi>[a-zA-Z0-9-]+)/(?P<ff>[a-zA-Z0-9-]+)$', reporte2.as_view(), name="reporte1"),
	url(r'reporte/(?P<ciudad>[a-zA-Z0-9-]+)/(?P<fi>[a-zA-Z0-9-]+)/(?P<ff>[a-zA-Z0-9-]+)$', 'reporteMoto', name="reporteMoto"),
)
