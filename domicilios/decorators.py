from django.core.exceptions import PermissionDenied
from functools import wraps
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from domicilios.models.users import Empleado
from django.shortcuts import HttpResponseRedirect

def administrador_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated():
            print 'se exploto 1'
            return redirect_to_login(next=request.get_full_path(), login_url=settings.LOGIN_URL)

        id = user.id
        print 'el usuario es %d'%id
        empleado1 = Empleado.objects.filter(id=id).first()
        print empleado1
        if empleado1 :
            if empleado1.cargo == 'ADMINISTRADOR' :
                return view_func(request, *args, **kwargs)
            #end if
        #end if
        raise PermissionDenied
        """
        try:
            empleado = Empleado.objects.get(id=id)
            print 'se exploto 2'
        except ObjectDoesNotExist:
            print 'se exploto 3'
            raise PermissionDenied

        if empleado.cargo != 'ADMINISTRADOR':
            print 'se exploto 4'
            raise PermissionDenied
        """
        

    return wrapper

def supervisor_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated():
            print 'se exploto 5'
            return redirect_to_login(next=request.get_full_path(), login_url=settings.LOGIN_URL)

        id = user.id

        try:
            empleado = Empleado.objects.get(pk=id)
        except ObjectDoesNotExist:
            print 'se exploto 6'
            raise PermissionDenied

        if empleado.cargo != 'ADMINISTRADOR' and empleado.cargo != 'SUPERVISOR':
            print 'se exploto 7'
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper

def alistador_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated():
            print 'se exploto 7'
            return redirect_to_login(next=request.get_full_path(), login_url=settings.LOGIN_URL)

        id = user.id

        try:
            empleado = Empleado.objects.get(pk=id)
        except ObjectDoesNotExist:
            print 'se exploto 8'
            raise PermissionDenied

        if empleado.cargo != 'ADMINISTRADOR' and empleado.cargo != 'SUPERVISOR' and empleado.cargo != 'ALISTADOR':
            print 'se exploto 9'
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper

def motorizado_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        print 'autenticacion del usuario %s '%user.is_authenticated(),request.get_full_path(),settings.LOGIN_URL
        if not user.is_authenticated():
            print 'se exploto 10'
            return redirect_to_login(next=request.get_full_path(), login_url=settings.LOGIN_URL)
        #endif
        if user.is_authenticated() and user.is_staff and user.is_active :
            print 'Este manes eladministrador'
            return HttpResponseRedirect('/soporte/')
        #end if

        id = user.id
        print 'usuario %d'%id,request.path
        try:
            empleado = Empleado.objects.filter(pk=id).first()
        except ObjectDoesNotExist:
            print 'se exploto 11'
            raise PermissionDenied
        if empleado :
            if empleado.cargo != 'ADMINISTRADOR' and empleado.cargo != 'SUPERVISOR' and empleado.cargo != 'ALISTADOR' and empleado.cargo != 'MOTORIZADO':
                print 'se exploto 12'
                raise PermissionDenied
            #end if
        #end if
        return view_func(request, *args, **kwargs)

    return wrapper
