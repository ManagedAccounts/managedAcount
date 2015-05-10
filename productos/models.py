from django.db import models
from formato.unidad_medida import u

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 200)
    codigo = models.PositiveIntegerField(default = 000)
    precio = models.DecimalField(decimal_places = 2, max_digits=3)
    stock = models.PositiveIntegerField(default = 0)
    unidad = models.CharField(max_length = 2, choices = u)

    def __str__(self):
        return u'%s' % self.descripcion
