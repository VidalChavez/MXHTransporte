from django.shortcuts import render

from rest_framework import viewsets

from transporte.models import Camion
from api.serializers import CamionSerializer


class CamionViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver y editar camiones.
    """
    queryset = Camion.objects.all()
    serializer_class = CamionSerializer
