from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from api import views




router = routers.DefaultRouter()
router.register(r'camiones', views.CamionViewSet)
router.register(r'rutas', views.RutaViewSet)
router.register(r'paradas', views.ParadaViewSet)

from transporte import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drove.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'drove.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
)
