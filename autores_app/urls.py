from django.urls import path
from  autores_app import views


urlpatterns = [
    path('autor', views.inicio_vistaAutores, name='autor'),
    path('registrarAutor/',views.registrarAutor,name='registrarAutor'),
    path('seleccionarAutor/<codigo>',views.seleccionarAutor,name='seleccionarAutor'),
    path('editarAutor/',views.editarAutor,name='editarAutor'),
    path('borrarAutor/<codigo>',views.borrarAutor,name='borrarAutor')
]