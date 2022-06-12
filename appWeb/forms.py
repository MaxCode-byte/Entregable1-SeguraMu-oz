from django import forms

class DjFormulario (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)   
    edad = forms.IntegerField()
    especialidad = forms.CharField(max_length=40)

class BartenderFormulario (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)   
    edad = forms.IntegerField()
    estilo = forms.CharField(max_length=40)

class MozoFormulario (forms.Form):        
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)   
    edad = forms.IntegerField()
    sector = forms.CharField(max_length=40)