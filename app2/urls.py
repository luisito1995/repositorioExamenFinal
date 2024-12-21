from django.urls import path
from . import views

app_name='app2'

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nuevoRegistro',views.nuevoRegistro,name='nuevoRegistro'),
    path('nuevaArea',views.nuevaArea,name='nuevaArea'),
    path('usuarios',views.usuarios,name='usuarios'),
    path('areas',views.areas,name='areas'),
    path('verArea/<str:idArea>',views.verArea,name='verArea')
]
