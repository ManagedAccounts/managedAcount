from django.db import models
from clientes.models import Cliente
from productos.models import Producto

from formato.tipos_comprobantes_pago import p
from formato.tipo_operaciones import q

# Create your models here.

class Venta(models.Model):
    tipo_comprobante = models.CharField(max_length=2, choices= p)
    text = models.CharField(max_length=20)
    zona = models.CharField(max_length=3, choices= q)
    cliente = models.ForeignKey(Cliente)
    serie = models.PositiveSmallIntegerField(default = 0)
    numero = models.PositiveIntegerField(default  = 0)
    #fecha = models.DateTimeField(auto_now_add = True)
    producto = models.ForeignKey(Producto)



    def __str__(self):
        return u'%s'% self.tipo_comprobante
