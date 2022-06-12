from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from appWeb.models import *       # Como se vio antes, from AppCoder(Carpeta).models(archivo dentro de la carpeta) import Curso(Funcion)
from appWeb.forms import *

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

#------------ Paginas de Forms ---------------

def djFormulario (request):
    if request.method == 'POST':
        djForm = DjFormulario(request.POST)
        print(djForm)
        if djForm.is_valid:       
            info = djForm.cleaned_data
            n = info['nombre']
            a = info['apellido']
            y = info['edad']
            e = info['especialidad']
            djs = dj(nombre=n, apellido=a, edad=y, especialidad=e)
            djs.save()
            return render(request, 'appWeb/inicio.html')
    else:
        djForm = DjFormulario()
    return render(request, 'appWeb/djFormulario.html', {'djForm':djForm})

def bartenderFormulario (request):
    if request.method == 'POST':
        bartenderForm = BartenderFormulario(request.POST)
        print(bartenderForm)
        if bartenderForm.is_valid:       
            info = bartenderForm.cleaned_data
            n = info['nombre']
            a = info['apellido']
            y = info['edad']
            t = info['estilo']
            bartenders = Bartender(nombre=n, apellido=a, edad=y, estilo=t)
            bartenders.save()
            return render(request, 'appWeb/inicio.html')
    else:
        bartenderForm = BartenderFormulario()
    return render(request, 'appWeb/bartenderFormulario.html', {'bartenderForm':bartenderForm})

def mozoFormulario (request):
    if request.method == 'POST':
        mozoForm = MozoFormulario(request.POST)
        print(mozoForm)
        if mozoForm.is_valid:       
            info = mozoForm.cleaned_data
            n = info['nombre']
            a = info['apellido']
            y = info['edad']
            s = info['sector']
            mozos = Mozo(nombre=n, apellido=a, edad=y, sector=s)
            mozos.save()
            return render(request, 'appWeb/inicio.html')
    else:
        mozoForm = MozoFormulario()
    return render(request, 'appWeb/mozoFormulario.html', {'mozoForm':mozoForm})


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


    
