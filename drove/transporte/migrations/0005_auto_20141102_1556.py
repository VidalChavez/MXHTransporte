# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0004_auto_20141102_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parada',
            name='ruta',
        ),
        migrations.AddField(
            model_name='ruta',
            name='parada',
            field=models.ManyToManyField(to='transporte.Ruta'),
            preserve_default=True,
        ),
    ]
