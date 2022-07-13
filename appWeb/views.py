
from pickle import NONE
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from appWeb.models import *       # Como se vio antes, from AppCoder(Carpeta).models(archivo dentro de la carpeta) import Curso(Funcion)
from appWeb.forms import *
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView 
from django.contrib.auth.mixins import *
from django.contrib.auth.decorators import *

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
@login_required
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

@login_required
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

@login_required
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

class djList (LoginRequiredMixin, ListView):
    model = dj
    template_name = 'appWeb/dj_list.html'

class BartenderList (LoginRequiredMixin, ListView):
    model = Bartender
    template_name = 'appWeb/Bartender.html'

class MozoList (LoginRequiredMixin, ListView):
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

class djCreate (LoginRequiredMixin, CreateView):
    model = dj
    success_url= reverse_lazy('dj_list')
    fields = ['nombre', 'apellido', 'edad', 'especialidad']

class BartenderCreate (LoginRequiredMixin, CreateView):
    model = Bartender
    success_url= reverse_lazy('Bartende_listr')
    fields = ['nombre', 'apellido', 'edad', 'estilo']

class MozoCreate (LoginRequiredMixin, CreateView):
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

#---------------------------------------------- Login ------------------------------
def login_request (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render (request, 'appWeb/loginHome.html', {'mensaje': f'Bienvenido {usuario}'})
            else:
                return render (request, 'appWeb/loginHome.html', {'mensaje': 'Datos incorrectos'})
        else: 
            return render (request, 'appWeb/loginHome.html',{'mensaje': 'Error en el Formulario'})
    else:
        form = AuthenticationForm()
        return render (request, 'appWeb/login.html', {'form': form})

#---------------------------------------------- Register ------------------------------

def register_request(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render (request, "appWeb/loginHome.html", {'mensaje': 'Usuario creado exitosamente'})
        else:
            return render (request, "appWeb/loginHome.html", {'mensaje': 'Error en la creacion del usuario'})   
    else: 
        form = UserRegistrationForm()
        return render (request, "appWeb/register.html", {'form': form}) 