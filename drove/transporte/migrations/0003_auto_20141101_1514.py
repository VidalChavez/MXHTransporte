# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0002_auto_20141101_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camion',
            name='num_pasajeros',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='camion',
            name='promedio_pasajeros',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='camion',
            name='promedio_tiempo',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='camion',
            name='velocidad',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parada',
            name='latitud',
            field=models.CharField(max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parada',
            name='longitud',
            field=models.CharField(max_length=140, blank=True),
            preserve_default=True,
        ),
    ]
