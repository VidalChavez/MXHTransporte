from rest_framework import serializers

from transporte.models import Camion, Parada, Ruta


class RutaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ruta
    

class CamionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Camion
        fields = ('identificador', 'velocidad', 'num_pasajeros', 'promedio_tiempo',
                  'promedio_pasajeros', 'ruta')
        
        
class ParadaSerializer(serializers.HyperlinkedModelSerializer):
    model = Ruta

    