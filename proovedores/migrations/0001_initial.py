# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.PositiveIntegerField(default=1)),
                ('percepcion', models.CharField(max_length=1, choices=[(b'j', b'Juridico'), (b'n', b'Natural')])),
                ('ruc', models.PositiveSmallIntegerField(default=12345678901)),
                ('direccion', models.CharField(max_length=200)),
                ('ubigeo', models.CharField(max_length=200)),
            ],
        ),
    ]
