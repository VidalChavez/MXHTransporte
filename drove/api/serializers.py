from rest_framework import serializers

from transporte.models import Camion, Parada, Ruta


class ParadaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parada


class RutaSerializer(serializers.HyperlinkedModelSerializer):
    #parada = ParadaSerializer(many=True)
    paradas = ParadaSerializer(many=True, )
    class Meta:
        model = Ruta



class CamionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Camion
        fields = ('identificador', 'velocidad', 'num_pasajeros', 'promedio_tiempo',
                  'promedio_pasajeros', 'ruta')
        
        

    