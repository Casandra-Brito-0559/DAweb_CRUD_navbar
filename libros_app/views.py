from django.shortcuts import render, redirect
from .models import Libros
# Create your views here.
def inicio_vistaLibros(request):
    loslibros=Libros.objects.all()
    return render(request, 'gestionLibros.html',{'mislibros':loslibros})
    
def registrarLibros(request):
    codigo = request.POST["txtcodigo"]
    titulo = request.POST["txttitulo"]
    autor = request.POST["txtautor"]
    genero = request.POST["txtgenero"]
    presio = request.POST["txtpresio"]
    cantidad = request.POST["numcantidad"]
    fecha = request.POST["datefecha"]

    guardarmateria = Libros.objects.create(codigo=codigo,titulo=titulo,autor=autor,genero=genero,presio=presio,cantidad=cantidad,fecha=fecha)
    return redirect('libro')

def seleccionarLibros(request, codigo):
    libro = Libros.objects.get(codigo=codigo)
    return render(request, 'editarLibros.html',{'mislibros':libro})

def editarLibros(request):
    codigo = request.POST["txtcodigo"]
    titulo = request.POST["txttitulo"]
    autor = request.POST["txtautor"]
    genero = request.POST["txtgenero"]
    presio = request.POST["txtpresio"]
    cantidad = request.POST["numcantidad"]
    fecha = request.POST["datefecha"]

    materia = Libros.objects.get(codigo=codigo)
    materia.titulo=titulo
    materia.autor=autor
    materia.genero=genero
    materia.presio=presio
    materia.cantidad=cantidad
    materia.fecha=fecha
    materia.save()
    return redirect('libro')

def borrarLibros(request, codigo):
    materia=Libros.objects.get(codigo=codigo)
    materia.delete()
    return redirect("libro")
