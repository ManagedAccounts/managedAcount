# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ruc', models.PositiveSmallIntegerField(default=0)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('ubigeo', models.CharField(max_length=200)),
                ('per', models.CharField(max_length=200)),
                ('cte', models.CharField(max_length=200)),
            ],
        ),
    ]
