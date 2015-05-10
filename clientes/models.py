from django.db import models

# Create your models here.

class Cliente(models.Model):
    ruc = models.PositiveSmallIntegerField(default=12345678901)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    ubigeo = models.CharField(max_length=200)
    per = models.CharField(max_length=200)
    cte = models.CharField(max_length=200)

    def __str__(self):
        return u'%s %s'% (self.ruc, self.nombre)
