from django.db import models
from domicilios.models.pedido import PedidoWS

class Punto(models.Model):
	latitud = models.FloatField()
	longitud = models.FloatField()

	def __unicode__(self):
		return '%d - %d'%(self.latitud,self.longitud)
	#end def
#end def

class Ruta(models.Model):
	inicio = models.FloatField()
	fin = models.FloatField()
	puntos = models.ManyToManyField(Punto)

	def __unicode__(self):
		return '%d - %d'%(self.inicio,self.fin)
	#end def
#end class

# Create your models here.
class Seguimiento(models.Model):
	pedido = models.ForeignKey(PedidoWS)
	ruta = models.OneToOneField(Ruta)

	def __unicode__(self):
		return '%s'%(self.pedido.num_pedido)
	#end def
#end class
