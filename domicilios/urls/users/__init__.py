from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^empleado/', include('domicilios.urls.users.empleado')),
	url(r'^cliente/', include('domicilios.urls.users.cliente')),
	url(r'^empresa/', include('domicilios.urls.users.empresa')),
	url(r'^user/', include('domicilios.urls.users.user')),
)
