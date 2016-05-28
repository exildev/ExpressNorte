# -*- coding: utf-8 -*-
from django.contrib.auth.views import login, logout
from domicilios.forms.users.userForm import LoginForm
from django.shortcuts import render, redirect,HttpResponse
from django.core.urlresolvers import reverse
from domicilios.decorators import *
from domicilios.models.users import Empleado
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def custom_login(request, **kwargs):
    print 'llegohasta aqui'
    if request.user.is_authenticated():
        return redirect(reverse('domicilios:index'))
    return login(request, authentication_form=LoginForm, **kwargs)

def custom_logout(request, **kwargs):
    # Current Django 1.6 uses GET to log out
    if not request.user.is_authenticated():
        return redirect(request.GET.get('next', reverse('domicilios:user-login')))

    del request.session["cargo"]
    del request.session["empresa"]

    return logout(request, **kwargs)

@motorizado_required
def index(request):
    userid = request.user.id
    empleado = Empleado.objects.filter(pk=userid).first()
    if not empleado :
        return redirect_to_login(next=request.get_full_path(), login_url=settings.LOGIN_URL)
    #end if
    cargo = empleado.cargo
    empresa = empleado.empresa.first_name
    request.session["cargo"] = cargo
    request.session["empresa"] = empresa
    if empresa == 'Express Del Norte':
        raise PermissionDenied
    else:
        return render(request,'api/users/User/index.html')

@motorizado_required
def rastreo(request):
    return render(request,'users/User/rastreo.html')

    
@csrf_exempt
def ws_loguin(request):
    username = request.POST.get('user',False)
    password = request.POST.get('password',False)
    if username and password :
        usuario = authenticate(username=username, password=password)
        if usuario :
            if usuario is not None:
                if usuario.is_active:
                    print 'si'
                    login(request, usuario)
                    return HttpResponse('true',content_type="application/json",status=200)
                else:
                    mensaje = "Usuario desactivado"
                #end if
            else:
                mensaje = "Usuario y/o Contraseña incorrectos"
            #end if
        #end if
    #end if
    return HttpResponse(mensaje,content_type="application/json",status=401)
#end def
