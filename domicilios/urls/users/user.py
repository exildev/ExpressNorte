from django.conf.urls import patterns, url
from django.contrib.auth.views import *

urlpatterns = patterns('domicilios.views.users.user',
                       url(r'^login/$', 'custom_login', {'template_name':'users/login.html'}, name='user-login'),
                       url(r'^logout/$', 'custom_logout', {'next_page': '/', }, name='user-logout'),
                       url(r'^ws/login/$','ws_loguin',name="ws_loguin"),
                    )
