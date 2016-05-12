from django.conf.urls import patterns, include, url

urlpatterns = patterns('domicilios.views.users.user',
	#Urls de Menus
	url(r'^$', 'index', name="api_index"),
	#Include de Vistas
	url(r'^users/', include('domicilios.urls.api.users')),
	url(r'^motorizado/', include('domicilios.urls.api.motorizado')),
	url(r'^pedido/', include('domicilios.urls.api.pedido')),
	url(r'^reporte/', include('domicilios.urls.api.reporte')),
)
