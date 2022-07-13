from urllib import request
from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User

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

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Comfirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name','last_name','email','password1','password2')
        help_text = {k:""for k in fields}