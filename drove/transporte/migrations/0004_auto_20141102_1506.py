# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0003_auto_20141101_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='camion',
            name='latitud',
            field=models.CharField(default=b'', max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='camion',
            name='longitud',
            field=models.CharField(default=b'', max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ruta',
            name='fin_lat',
            field=models.CharField(default=b'', max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ruta',
            name='fin_long',
            field=models.CharField(default=b'', max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ruta',
            name='inicio_lat',
            field=models.CharField(default=b'', max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ruta',
            name='inicio_long',
            field=models.CharField(default=b'', max_length=140, blank=True),
            preserve_default=True,
        ),
    ]
