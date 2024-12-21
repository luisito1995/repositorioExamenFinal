from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class datosUsuario(models.Model):
    profesion = models.CharField(max_length=48,null=True,blank=True)
    nroCelular = models.CharField(max_length=16,null=True,blank=True)
    perfilUsuario = models.CharField(max_length=256,null=True,blank=True)
    usrRel = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)

class publicacion(models.Model):
    titulo = models.CharField(max_length=64,null=True,blank=True)
    descripcion = models.CharField(max_length=256,null=True,blank=True)
    autorPub = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    imagenPub = models.ImageField(upload_to='imagenes/',null=True, blank=True)

class comentario(models.Model):
    descripcion = models.CharField(max_length=256,null=True,blank=True)
    pubRel = models.ForeignKey(publicacion, on_delete=models.CASCADE, null=True, blank=True)
    autoCom = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
