from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models.users import Cliente, Empleado, Empresa
from .models.motorizado import Moto, Soat, Tecno, Motorizado
from .models.pedido import Pedido, Items, Tiempo, ItemsPedido,Tiempo
from django.contrib.auth.forms import UserCreationForm
from domicilios.forms.users.clienteForm import *
from domicilios.forms.users.empleadoForm import * 
# Register your models here.

#Administracion de Cliente
class ClienteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion Personal', {'fields': ['first_name', 'last_name', 'tipo_id', 'identificacion']}),
        ('Informacion de Contacto', {'fields': ['telefono_fijo', 'telefono_celular', 'direccion', 'barrio', 'zona']}),
    ]
    list_display = ('first_name',)

    

admin.site.register(Cliente, ClienteAdmin)

#Administracion de Empleado
class EmpleadoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion Personal', {'fields': ['username','first_name', 'last_name', 'tipo_id', 'identificacion', 'cargo', 'fecha_nacimiento', 'empresa', 'is_active']}),
        ('Informacion de Contacto', {'fields': ['telefono_fijo', 'telefono_celular', 'email','direccion','ciudad']}),
    ]
    list_display = ('first_name', 'last_name', 'cargo', 'empresa',)



admin.site.register(Empleado, EmpleadoAdmin)

#Administracion de Empresa
class EmpresaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion Empresarial', {'fields': ['nit','first_name', 'logo', 'web', 'username','active']}),
    ]

admin.site.register(Empresa, EmpresaAdmin)

#Administracion de Motorizado
class MotorizadoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion del Motorizado', {'fields': ['empleado', 'licencia', 'moto']}),
    ]
    list_display = ('empleado', 'moto',)
admin.site.register(Motorizado, MotorizadoAdmin)

#Administracion de Moto
class MotoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion de Automotor', {'fields': ['tipo','marca', 'placa','empresaM']}),
        ('Documentacion', {'fields': ['t_propiedad', 'soat', 'tecno']}),
    ]
    list_display = ('placa', 'empresaM',)
admin.site.register(Moto, MotoAdmin)

#Administracion de Soat
class SoatAdmin(admin.ModelAdmin):
    pass
admin.site.register(Soat, SoatAdmin)

#Administracion de Tecno
class TecnoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tecno, TecnoAdmin)

#Administracion de Pedido
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'empresaI',)
admin.site.register(Items, ItemsAdmin)

#Administracion de Pedido
class ItemsList(admin.StackedInline):
    model = ItemsPedido
    extra = 1

class TiempoAdmin(admin.TabularInline):
    model = Tiempo
    exta = 1

class PedidoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion General', {'fields': ['num_pedido', 'npedido_express','tienda', 'cliente','observacion']}),
        ('Usuarios de Servicio', {'fields': ['supervisor', 'alistador', 'motorizado', 'empresa', 'total']}),
    ]
    inlines = [TiempoAdmin, ItemsList]
    list_display = ('num_pedido', 'fecha_pedido', 'npedido_express')

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Tiempo)

#Administracion de User y Group
#admin.site.unregister(User)
#admin.site.unregister(Group)
