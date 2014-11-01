# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificador', models.CharField(max_length=32)),
                ('velocidad', models.IntegerField(null=True)),
                ('num_pasajeros', models.IntegerField(null=True)),
                ('promedio_tiempo', models.FloatField(null=True)),
                ('promedio_pasajeros', models.FloatField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_parada', models.CharField(max_length=25)),
                ('longitud', models.CharField(max_length=140)),
                ('latitud', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_ruta', models.CharField(max_length=25)),
                ('num_camiones', models.IntegerField(null=True, blank=True)),
                ('num_pasajeros', models.IntegerField(null=True, blank=True)),
                ('promedio_personas', models.FloatField(null=True, blank=True)),
                ('promedio_personas_camion', models.FloatField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='parada',
            name='ruta',
            field=models.ManyToManyField(to='transporte.Ruta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='camion',
            name='ruta',
            field=models.ForeignKey(to='transporte.Ruta'),
            preserve_default=True,
        ),
    ]
