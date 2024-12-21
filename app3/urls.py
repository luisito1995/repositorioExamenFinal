from django.urls import path
from . import views

app_name='app3'

urlpatterns = [
    path('',views.ingresoUsuario,name='ingresoUsuario'),
    path('informacionUsuario',views.informacionUsuario,name='informacionUsuario'),
    path('cerrarSesion',views.cerrarSesion,name='cerrarSesion'),
    path('ejemploJs',views.ejemploJs,name='ejemploJs'),
    path('devolverDatos',views.devolverDatos,name='devolverDatos'),
    path('devolverAllPubs',views.devolverAllPubs,name='devolverAllPubs'),
    path('devolverPublicacion',views.devolverPublicacion,name='devolverPublicacion'),
    path('publicarComentario',views.publicarComentario,name='publicarComentario'),
    path('crearPublicacion', views.crearPublicacion, name='crearPublicacion'),
    path('inicioReact', views.inicioReact, name='inicioReact'),
    
    #RUTA CONSOLA ADMINISTRADOR - EXAMEN FINAL
    path('consolaAdministrador',views.consolaAdministrador,name='consolaAdministrador'),
    path('registrarUsuario', views.registrarUsuario, name='registrarUsuario'),
    #RUTA ACTUALIZARUSUARIO, OBTENERDATOSUSUARIO - EXAMEN FINAL
    path('obtenerDatosUsuario',views.obtenerDatosUsuario,name='obtenerDatosUsuario'),
    path('actualizarUsuario',views.actualizarUsuario,name='actualizarUsuario')  

]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  