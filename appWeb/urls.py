
from unicodedata import name
from django.urls import path
from appWeb.views import *

urlpatterns = [
    #------------- Inicios ------------
    path('', inicio, name= 'inicio'),
    path('djs/', Djs, name= 'djsinicio'),
    path('bartenders/', Bartenders, name= 'bartendersinicio'),
    path('mozos/', Mozos, name= 'mozosinicio'),
    #------------- Formularios ------------
    path('djFormulario/', djFormulario, name='djFormulario'),
    path('bartenderFormulario/', bartenderFormulario, name='bartenderFormulario'),
    path('mozoFormulario/', mozoFormulario, name='mozoFormulario'),
    #------------- Buscadores ------------
    path('djBusqueda/', djBusqueda, name='djBusqueda'),
    path('buscarDj/', djbuscar, name= 'djBuscar'),
    path('bartenderBusqueda/', bartenderBusqueda, name='bartenderBusqueda'),
    path('buscarBartender/', bartenderbuscar, name='bartenderBuscar'),
    path('mozoBusqueda/',mozoBusqueda, name='mozoBusqueda'),
    path('buscarMozo/',mozobuscar, name='mozoBuscar')
    
    
]
