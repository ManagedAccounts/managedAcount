from django.db import models

from format.tipos_comprobantes_pago import p

# Create your models here.

class Venta(models.Model):
    tipo_comprobante = models.CharField(max_length = 2, choices = p,)
    texto = models.CharField(max_length = 20)
    #numero_registro = models.IntegerField(max_length = 20)


    def __str__(self):
        return u'%s' % (self.texto)
