from django.conf.urls import patterns, include, url

urlpatterns = patterns('domicilios.views.users.user',
	#Urls de Menus
	url(r'^$', 'index', name="index"),
	url(r'^rastreo/', 'rastreo', name="rastreo"),
	#Include de Vistas
	url(r'^users/', include('domicilios.urls.users')),
	url(r'^motorizado/', include('domicilios.urls.motorizado')),
	url(r'^pedido/', include('domicilios.urls.pedido')),
	url(r'^plataforma/', include('domicilios.urls.api')),
)
