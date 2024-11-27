from django.urls import path
from  libros_app import views


urlpatterns = [
    path('libro', views.inicio_vistaLibros, name='libro'),
    path('registrarLibros/',views.registrarLibros,name='registrarLibros'),
    path('seleccionarLibros/<codigo>',views.seleccionarLibros,name='seleccionarLibros'),
    path('editarLibros/',views.editarLibros,name='editarLibros'),
    path('borrarLibros/<codigo>',views.borrarLibros,name='borrarLibros')
]