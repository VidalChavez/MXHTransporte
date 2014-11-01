from django.contrib import admin

from transporte.models import Camion, Parada, Ruta

admin.site.register(Camion)
admin.site.register(Parada)
admin.site.register(Ruta)

# Register your models here.
