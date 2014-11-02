# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0005_auto_20141102_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruta',
            name='parada',
        ),
        migrations.AddField(
            model_name='parada',
            name='ruta',
            field=models.ForeignKey(related_name='paradas', to='transporte.Ruta', null=True),
            preserve_default=True,
        ),
    ]
