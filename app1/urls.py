from django.urls import path
from . import views

app_name='app1'

urlpatterns = [
    path('',views.hola,name='hola'),
    path('primerhtml',views.primerhtml,name='primerhtml'),
    path('segundohtml',views.segundohtml,name='segundohtml')
]
