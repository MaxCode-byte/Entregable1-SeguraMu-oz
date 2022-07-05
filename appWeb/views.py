from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from appWeb.models import *       # Como se vio antes, from AppCoder(Carpeta).models(archivo dentro de la carpeta) import Curso(Funcion)
from appWeb.forms import *
from django.views.generic import *
from django.urls import reverse_lazy

#------------ Pagina de inicio---------------

def inicio(self):
    plantilla = loader.get_template('appWeb/inicio.html')   # El inicio siempre tiene que tener un loader
    documento = plantilla.render()
    return HttpResponse(documento)

#------------ Paginas de personal (INICIO) ---------------

def Djs (request):
    return render(request, 'appWeb/djsinicio.html')

def Bartenders (request):
    return render(request, 'appWeb/bartendersinicio.html')

def Mozos (request):
    return render(request, 'appWeb/mozosinicio.html')



#------------ Paginas de Busqueda ---------------

def djBusqueda (request):
    return render(request, 'appWeb/djBusqueda.html')

def djbuscar (request):
    if request.GET ['Especialidad']:
        spec = request.GET ['Especialidad']
        Dj = dj.objects.filter(especialidad=spec)            
        return render(request, 'appWeb/djResultado.html', {'nombre':Dj, 'especialidad':spec}) 
    else:
        respuesta =  "No enviaste datos"
    return HttpResponse(respuesta) 

def bartenderBusqueda (request):
    return render(request, 'appWeb/bartenderBusqueda.html')

def bartenderbuscar (request):
    if request.GET ['Estilo']:
        coctelery = request.GET ['Estilo']
        Bart = Bartender.objects.filter(estilo=coctelery)            
        return render(request, 'appWeb/bartenderResultado.html', {'nombre':Bart, 'estilo':coctelery}) 
    else:
        respuesta =  "No enviaste datos"
    return HttpResponse(respuesta) 


def mozoBusqueda (request):
    return render(request, 'appWeb/mozoBusqueda.html')

def mozobuscar (request):
    if request.GET ['Sector']:
        sect = request.GET ['Sector']
        Waiter = Mozo.objects.filter(sector=sect)          
        return render(request, 'appWeb/mozoResultado.html', {'nombre':Waiter, 'sector':sect}) 
    else:
        respuesta =  "No enviaste datos"
    return HttpResponse(respuesta) 


#---------------------------------------------- Vistas por clases ------------------------------


#---------------------------------------------- Read ------------------------------

class djList (ListView):
    model = dj
    template_name = 'appWeb/dj_list.html'

class BartenderList (ListView):
    model = Bartender
    template_name = 'appWeb/Bartender.html'

class MozoList (ListView):
    model = Mozo
    template_name= 'appWeb/Mozo.html'

#---------------------------------------------- Detail ------------------------------

class djDetail (DetailView):
    model = dj
    template_name= 'appWeb/dj_Detalle.html'

class BartenderDetail (DetailView):
    model = Bartender
    template_name= 'appWeb/Bartender_Detalle.html'

class MozoDetail (DetailView):
    model = Mozo
    template_name= 'appWeb/Mozo_Detalle.html'

#---------------------------------------------- Create ------------------------------

class djCreate (CreateView):
    model = dj
    success_url= reverse_lazy('dj_list')
    fields = ['nombre', 'apellido', 'edad', 'especialidad']

class BartenderCreate (CreateView):
    model = Bartender
    success_url= reverse_lazy('Bartende_listr')
    fields = ['nombre', 'apellido', 'edad', 'estilo']

class MozoCreate (CreateView):
    model = Mozo
    success_url= reverse_lazy('Mozo_list')
    fields = ['nombre', 'apellido', 'edad', 'sector']

#---------------------------------------------- Update ------------------------------

class djUpdate (UpdateView):
    model = dj
    success_url= reverse_lazy('dj_list')
    fields = ['nombre', 'apellido', 'edad', 'especialidad']
class BartenderUpdate (UpdateView):
    model = Bartender
    success_url= reverse_lazy('Bartender_list')
    fields = ['nombre', 'apellido', 'edad', 'estilo']

class MozoUpdate (UpdateView):
    model = Mozo
    success_url= reverse_lazy('Mozo_list')
    fields = ['nombre', 'apellido', 'edad', 'sector']

#---------------------------------------------- Update ------------------------------

class djDelete (DeleteView):
    model = dj
    success_url= reverse_lazy('dj_list')
    
class BartenderDelete (DeleteView):
    model = Bartender
    success_url= reverse_lazy('Bartender_list')
   

class MozoDelete (DeleteView):
    model = Mozo
    success_url= reverse_lazy('Mozo_list')
    