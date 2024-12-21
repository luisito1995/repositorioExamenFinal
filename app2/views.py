from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import usuario,area


# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def nuevoRegistro(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        numeroUsuario = request.POST.get('numeroUsuario')
        direccionUsuario = request.POST.get('direccionUsuario')
        areaSeleccionada = request.POST.get('areaSeleccionada')
        areaObj = area.objects.get(id=areaSeleccionada)
        usuario.objects.create(
            nombreUsuario=nombreUsuario,
            numeroUsuario=numeroUsuario,
            direccionUsuario=direccionUsuario,
            areaR=areaObj
        )
        return HttpResponseRedirect(reverse('app2:usuarios'))
    return render(request,'nuevoRegistro.html',{
        'areasSistema':area.objects.all()
    })

def nuevaArea(request):
    if request.method == 'POST':
        nombreArea = request.POST.get('nombreDireccion')
        descripcionArea = request.POST.get('descripcionDireccion')
        area.objects.create(
            nombreArea=nombreArea,
            descripcionArea=descripcionArea
        )
        return HttpResponseRedirect(reverse('app2:areas'))
    return render(request,'nuevaArea.html',{
        'areasSistema':area.objects.all()
    })

def usuarios(request):
    usuariosTotales = usuario.objects.all()
    return render(request,'usuarios.html',{
        'usuariosTotales':usuariosTotales,
        'areasSistema':area.objects.all()
    })

def areas(request):
    areasTotales = area.objects.all()
    return render(request,'areas.html',{
        'areasTotales':areasTotales,
        'areasSistema':area.objects.all()
    })

def verArea(request,idArea):
    areaInfo = area.objects.get(id=idArea)
    listaUsuarios = areaInfo.usuario_set.all()
    return render(request,'verArea.html',{
        'objArea':areaInfo,
        'areasSistema':area.objects.all(),
        'listaUsuarios':listaUsuarios
    })