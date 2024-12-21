from django.db import models

class area(models.Model):
    nombreArea = models.CharField(max_length=32, null=True, blank=True)
    descripcionArea = models.CharField(max_length=256, null=True, blank=True)

# Create your models here.
class usuario(models.Model):
    nombreUsuario = models.CharField(max_length=64, null=True, blank=True)
    numeroUsuario = models.CharField(max_length=32, null=True, blank=True)
    direccionUsuario = models.CharField(max_length=64, null=True, blank=True)
    areaUsuario = models.CharField(max_length=32, null=True, blank=True)
    descripcionUsuario = models.CharField(max_length=256, null=True, blank=True)
    areaR = models.ForeignKey(area, null=True, blank=True, on_delete=models.SET_NULL)

