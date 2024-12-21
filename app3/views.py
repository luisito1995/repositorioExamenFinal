from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse, FileResponse
from django.urls import reverse
from .models import publicacion, comentario, datosUsuario
import json
import base64
from django.contrib.auth.models import User


def ingresoUsuario(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        usrObj = authenticate(request,username=nombreUsuario, password=contraUsuario)
        if usrObj is not None:
            login(request,usrObj)
            return HttpResponseRedirect(reverse('app3:informacionUsuario'))
        else:
            return HttpResponseRedirect(reverse('app3:ingresoUsuario'))
    return render(request,'ingresoUsuario.html')

@login_required(login_url='/')
def informacionUsuario(request):
    return render(request,'informacionUsuario.html',{
        'allPubs':publicacion.objects.all()
    })


@login_required(login_url='/')
def cerrarSesion(request):
    logout(request)
    return render(request,'ingresoUsuario.html')

def ejemploJs(request):
    return render(request,'ejemploJs.html')

def devolverDatos(request):
    return JsonResponse(
        {
            'nombreCurso':'DesarroloWebPython',
            'horario':{
                'martes':'7-10',
                'jueves':'7-10'
            },
            'backend':'django',
            'frontend':'reactjs',
            'cantHoras':24
        }
    )

def devolverAllPubs(request):
    objPub = publicacion.objects.all()
    listaPublicacion = []
    for obj in objPub:
        listaPublicacion.append(
            {
                'titulo':obj.titulo,
                'descripcion':obj.descripcion
            }
        )
    return JsonResponse({
        'listaPublicacion':listaPublicacion
    })

def devolverPublicacion(request):
    idPub = request.GET.get('idPub')
    try:
        datosComentarios = []
        objPub = publicacion.objects.get(id=idPub)
        comentariosPub = objPub.comentario_set.all()
        for comentarioInfo in comentariosPub:
            datosComentarios.append({
                'autor': f"{comentarioInfo.autoCom.first_name} {comentarioInfo.autoCom.last_name}",
                'descripcion': comentarioInfo.descripcion
            })
        try:
            with open(objPub.imagenPub.path,'rb') as imgFile:
                imgPub = base64.b64encode(imgFile.read()).decode('UTF-8')
        except:
            imgPub = None

        return JsonResponse({
            'titulo': objPub.titulo,
            'autor':f"{objPub.autorPub.first_name} {objPub.autorPub.last_name}",
            'descripcion':objPub.descripcion,
            'datosComentarios': datosComentarios,
            'imgPub':imgPub
        })
    except:
        return JsonResponse({
            'titulo':'SIN DATOS',
            'autor':'SIN DATOS',
            'descripcion':'SIN DATOS',
            'datosComentarios':None,
            'imgPub':None
        })
    
def publicarComentario(request):
    datosComentario = json.load(request)
    print(datosComentario)
    comentarioTexto = datosComentario.get('comentario')
    idPublicacion = datosComentario.get('idPublicacion')
    objPublicacion = publicacion.objects.get(id=idPublicacion)
    comentario.objects.create(
        descripcion = comentarioTexto,
        pubRel = objPublicacion,
        autoCom = request.user
    )
    return JsonResponse({
        'resp':'ok'
    })

def crearPublicacion(request):
    if request.method == 'POST':
        tituloPub = request.POST.get('tituloPub')
        descripcionPub = request.POST.get('descripcionPub')
        autorPub = request.user
        imagenPub = request.FILES.get('imagenPub')

        publicacion.objects.create(
            titulo=tituloPub,
            descripcion=descripcionPub,
            autorPub = autorPub,
            imagenPub = imagenPub
        )

        return HttpResponseRedirect(reverse('app3:informacionUsuario'))
    
def inicioReact(request):
    return render(request, 'inicioReact.html')


@login_required(login_url='/')
def registrarUsuario(request):
    if request.method == 'POST':
        # Capturar los datos del formulario
        usernameUsuario = request.POST.get('usernameUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        nombreUsuario = request.POST.get('nombreUsuario')
        apellidoUsuario = request.POST.get('apellidoUsuario')
        emailUsuario = request.POST.get('emailUsuario')
        profesionUsuario = request.POST.get('profesionUsuario')
        nroCelular = request.POST.get('nroCelular')
        perfilUsuario = request.POST.get('perfilUsuario')

        # Verificar los datos recibidos
        print(f'Datos recibidos: {usernameUsuario}, {contraUsuario}, {nombreUsuario}, {apellidoUsuario}, {emailUsuario}, {profesionUsuario}, {nroCelular}, {perfilUsuario}')


        # Crear el objeto User
        nuevoUsuario = User.objects.create(
            username=usernameUsuario,
            email=emailUsuario
        )
        nuevoUsuario.set_password(contraUsuario)
        nuevoUsuario.first_name = nombreUsuario
        nuevoUsuario.last_name = apellidoUsuario
        nuevoUsuario.is_staff = True  # Permitir acceso al administrador
        nuevoUsuario.save()

        # Verifica si el usuario se guarda correctamente
        print(f'Nuevo Usuario creado: {nuevoUsuario.username}')

        # Crear el registro en datosUsuario y asociarlo
        datosUsuario.objects.create(
            profesion=profesionUsuario,
            nroCelular=nroCelular,
            perfilUsuario=perfilUsuario,
            usrRel=nuevoUsuario
        )

        # Verifica si el objeto datosUsuario se crea correctamente
        print(f'Nuevo registro en datosUsuario creado para: {nuevoUsuario.username}')

        # Redirigir a la consola de administrador
        return HttpResponseRedirect(reverse('app3:consolaAdministrador'))

    # Si no es un método POST, devolver un error o redirigir
    return HttpResponseRedirect(reverse('app3:consolaAdministrador'))


@login_required(login_url='/')
def consolaAdministrador(request):
    allUsers = User.objects.all().order_by('id')
    return render(request,'consolaAdministrador.html',{
        'allUsers':allUsers
    })

@login_required(login_url='/')
def obtenerDatosUsuario(request):
    idUsuario = request.GET.get('idUsuario')

     # Verificar si el idUsuario está presente y es válido
    if not idUsuario or not idUsuario.isdigit():
        return JsonResponse({'resp': '400', 'mensaje': 'ID de usuario inválido o no proporcionado'})

    try:
        # Obtener el objeto User
        usuario = User.objects.get(id=idUsuario)
        # Obtener los datos relacionados de datosUsuario
        datos_usuario = datosUsuario.objects.get(usrRel=usuario)

        # Crear respuesta JSON con los datos necesarios
        return JsonResponse({
            'resp': '200',
            'username': usuario.username,
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'profesion': datos_usuario.profesion,
            'nroCelular': datos_usuario.nroCelular,
            'perfilUsuario': datos_usuario.perfilUsuario,
        })
    except User.DoesNotExist:
        return JsonResponse({'resp': '404', 'mensaje': 'Usuario no encontrado'})
    except datosUsuario.DoesNotExist:
        return JsonResponse({'resp': '404', 'mensaje': 'Datos del usuario no encontrados'})


@login_required(login_url='/')
def actualizarUsuario(request):
    if request.method == 'POST':
        # Obtener el idUsuario desde el formulario
        idUsuario = request.POST.get('idUsuario')
        
        if not idUsuario:
            return JsonResponse({'resp': '400', 'mensaje': 'ID de usuario no proporcionado'})
        
        try:
            # Obtener los objetos User y datosUsuario
            usuario = User.objects.get(id=idUsuario)
            datos_usuario = datosUsuario.objects.get(usrRel=usuario)
            
            # Actualizar los datos del usuario
            usuario.first_name = request.POST.get('first_name', usuario.first_name)
            usuario.last_name = request.POST.get('lastName', usuario.last_name)
            usuario.email = request.POST.get('email', usuario.email)
            usuario.save()  # Guardar cambios en el modelo User
            
            # Actualizar los datos adicionales
            datos_usuario.profesion = request.POST.get('profesion', datos_usuario.profesion)
            datos_usuario.nroCelular = request.POST.get('nroCelular', datos_usuario.nroCelular)
            datos_usuario.perfilUsuario = request.POST.get('perfilUsuario', datos_usuario.perfilUsuario)
            datos_usuario.save()  # Guardar cambios en el modelo datosUsuario
            
            return HttpResponseRedirect(reverse('app3:consolaAdministrador'))
        
        except User.DoesNotExist:
            return JsonResponse({'resp': '404', 'mensaje': 'Usuario no encontrado'})
        except datosUsuario.DoesNotExist:
            return JsonResponse({'resp': '404', 'mensaje': 'Datos del usuario no encontrados'})
    
    return JsonResponse({'resp': '400', 'mensaje': 'Método no permitido'})


