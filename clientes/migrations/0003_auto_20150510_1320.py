# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20150510_0500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cte',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='per',
        ),
        migrations.AddField(
            model_name='cliente',
            name='percepcion',
            field=models.CharField(default=18, max_length=1, choices=[(b'j', b'Juridico'), (b'n', b'Natural')]),
            preserve_default=False,
        ),
    ]
