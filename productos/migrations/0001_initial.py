# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('codigo', models.PositiveIntegerField(default=0)),
                ('precio', models.DecimalField(max_digits=3, decimal_places=3)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('unidad', models.CharField(max_length=2, choices=[(b'01', b'KILOGRAMOS'), (b'02', b'LIBRAS'), (b'03', b'TONELADAS LARGAS'), (b'04', b'TONELADAS M\xc3\x89TRICAS'), (b'05', b'TONELADAS CORTAS'), (b'06', b'GRAMOS'), (b'07', b'UNIDADES'), (b'08', b'LITROS'), (b'09', b'GALONES'), (b'10', b'BARRILES'), (b'11', b'LATAS'), (b'12', b'CAJAS'), (b'13', b'MILLARES'), (b'14', b'METROS CUBICOS'), (b'15', b'METROS'), (b'99', b'OTROS')])),
            ],
        ),
    ]
