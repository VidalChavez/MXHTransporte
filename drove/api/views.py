from django.shortcuts import render

from rest_framework import viewsets

from transporte.models import Camion, Ruta, Parada
from api.serializers import CamionSerializer, RutaSerializer, ParadaSerializer


class CamionViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver y editar camiones.
    """
    queryset = Camion.objects.all()
    serializer_class = CamionSerializer
    
    
class RutaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver y editar rutas.
    """
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer


class ParadaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver y editar Paradas.
    """
    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer
