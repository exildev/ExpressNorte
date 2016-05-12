from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^', include('domicilios.urls.pedido.pedido')),
)
