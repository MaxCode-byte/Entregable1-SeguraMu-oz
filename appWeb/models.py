
from django.db import models

# Create 3 models aca 
# Tematica: Personal de club nocturno

class dj (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)   
    edad = models.IntegerField()
    especialidad = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nombre +' '+ self.especialidad

class Bartender (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)   
    edad = models.IntegerField()
    estilo = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.nombre +' '+ self.estilo


class Mozo (models.Model):        
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)   
    edad = models.IntegerField()
    sector = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.nombre +' '+ self.sector