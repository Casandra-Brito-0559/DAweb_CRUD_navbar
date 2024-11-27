from django.shortcuts import render, redirect
from .models import Autores
# Create your views here.
def inicio_vistaAutores(request):
    losautores=Autores.objects.all()
    return render(request, 'gestionAutor.html',{'misautores':losautores})
    
def registrarAutor(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellidos = request.POST["txtapellidos"]
    librose = request.POST["numlibrose"]
    contacto = request.POST["txtcontacto"]
    pais = request.POST["txtpais"]
    popularidad=request.POST["txtpopularidad"]

    guardarmateria = Autores.objects.create(codigo=codigo,nombre=nombre,apellidos=apellidos,librose=librose,contacto=contacto,pais=pais,popularidad=popularidad)
    return redirect('autor')

def seleccionarAutor(request, codigo):
    autor = Autores.objects.get(codigo=codigo)
    return render(request, 'editarAutor.html',{'misautores':autor})

def editarAutor(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellidos = request.POST["txtapellidos"]
    librose = request.POST["numlibrose"]
    contacto = request.POST["txtcontacto"]
    pais = request.POST["txtpais"]
    popularidad=request.POST["txtpopularidad"]

    materia = Autores.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.apellidos=apellidos
    materia.librose=librose
    materia.contacto=contacto
    materia.pais=pais
    materia.popularidad=popularidad
    
    materia.save()
    return redirect('autor')

def borrarAutor(request, codigo):
    materia=Autores.objects.get(codigo=codigo)
    materia.delete()
    return redirect('autor')