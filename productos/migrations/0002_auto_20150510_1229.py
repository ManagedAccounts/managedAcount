# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.CharField(default=17, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(max_digits=3, decimal_places=2),
        ),
    ]
