from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from transporte.models import Ruta, Camion, Parada


def index(request):
    
    context = RequestContext(request)
    
    lista_rutas = Ruta.objects.all()
    print lista_rutas
    context_dict = {'rutas':lista_rutas}
    
    return render_to_response('prueba.html', context_dict, context)
    


