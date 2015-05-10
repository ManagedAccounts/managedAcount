from django.db import models

from formato.tipos_comprobantes_pago import p
from formato.tipo_operaciones import q

# Create your models here.

class Compra(models.Model):
    tipo_c = models.CharField(max_length = 2, choices = p)
    tet = models.CharField(max_length = 20)

    def __str__(self):
        return u'%s' % self.tet
