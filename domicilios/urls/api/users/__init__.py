from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^empleado/', include('domicilios.urls.api.users.empleado')),
	url(r'^cliente/', include('domicilios.urls.api.users.cliente')),
)
