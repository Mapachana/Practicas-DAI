from django.db import models


# galerias/models.py

from django.utils import timezone
  
class Galeria(models.Model):
  nombre     = models.CharField(max_length=200)
  dirección  = models.CharField(max_length=100)
  ... 
  
  def __str__(self):
    return self.nombre
  
class Cuadro(models.Model):
  nombre           = models.CharField(max_length=100)
  galeria          = models.ForeignKey(Galeria, on_delete=models.CASCADE)
  autor            = models.CharField(max_length=100)
  fecha_creación   = models.DateField(default=timezone.now)
  ...
  