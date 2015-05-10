from django.db import models

# Create your models here.

p=(
    ('j','Juridico'),
    ('n','Natural'),
)

class Cliente(models.Model):
    ruc = models.PositiveSmallIntegerField(default=12345678901)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    percepcion = models.CharField(max_length = 1, choices = p)
    ubigeo = models.CharField(max_length=200)

    def __str__(self):
        return u'%s %s'% (self.nombre, self.ruc)
