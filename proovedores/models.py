from django.db import models

# Create your models here.
p=(
    ('j','Juridico'),
    ('n','Natural'),
)
class Proveedor(models.Model):
    nombre = models.CharField(max_length = 200)
    codigo = models.PositiveIntegerField(default= 001)
    percepcion = models.CharField(max_length = 1, choices = p)
    ruc = models.PositiveSmallIntegerField(default=12345678901)
    direccion = models.CharField(max_length=200)
    ubigeo = models.CharField(max_length=200)

    def __str__(self):
        return u'%s %s' % (self.nombre, self.ruc)
