from django.db import models


class Ruta(models.Model):
    nombre_ruta = models.CharField(max_length=25)
    num_camiones = models.IntegerField(blank=True, null=True)
    num_pasajeros = models.IntegerField(blank=True, null=True)
    promedio_personas = models.FloatField(blank=True, null=True)
    promedio_personas_camion = models.FloatField(blank=True, null=True)
    
    def __unicode__(self):
        return self.nombre_ruta
    
    
class Parada(models.Model):
    nombre_parada = models.CharField(max_length=25)
    longitud = models.CharField(max_length=140)
    latitud = models.CharField(max_length=140)
    ruta = models.ManyToManyField('Ruta')
    
    def __unicode__(self):
        return self.nombre_parada
    

class Camion(models.Model):
    identificador = models.CharField(max_length=32)
    velocidad = models.IntegerField(null=True)
    num_pasajeros = models.IntegerField(null=True)
    promedio_tiempo = models.FloatField(null=True)
    promedio_pasajeros = models.FloatField(null=True)
    ruta = models.ForeignKey('Ruta')
    
    class Meta:
        verbose_name_plural = "Camiones"
    
    
    def __unicode__(self):
        return self.identificador
    
    


