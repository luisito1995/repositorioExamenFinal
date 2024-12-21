from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse

# Create your views here.
def hola(request):
    return HttpResponse("Bienvenidos a mi web")

def primerhtml(request):
    nombre = "Martin"
    rol = 'USUARIO'
    apellido='Segovia'
    listaEstudiantes = [
        'Javier Hilario',
        'Dante Arroyo',
        'Jorge Ramirez',
        'Alexander Segovia'
    ]
    return render(request,'primerhtml.html',{
        'nombre':nombre,
        'rol':rol,
        'estudiantes':listaEstudiantes
    })

def segundohtml(request):
    nombre = "Alexander"
    return render(request,'segundohtml.html')
