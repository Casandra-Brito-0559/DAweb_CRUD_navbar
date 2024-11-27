from django.shortcuts import render, redirect
from .models import Sucursales
# Create your views here.
def inicio_vistaSucursales(request):
    lossucursales=Sucursales.objects.all()
    return render(request, 'gestionSucursal.html',{'missucursales':lossucursales})
    
def registrarSucursal(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    horario = request.POST["txthorario"]
    encargado = request.POST["txtencargado"]
    

    guardarmateria = Sucursales.objects.create(codigo=codigo,nombre=nombre,direccion=direccion,telefono=telefono,correo=correo,horario=horario,encargado=encargado)
    return redirect('sucursal')

def seleccionarSucursal(request, codigo):
    sucursal = Sucursales.objects.get(codigo=codigo)
    return render(request, 'editarSucursal.html',{'misucursales':sucursal})

def editarSucursal(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    horario = request.POST["txthorario"]
    encargado = request.POST["txtencargado"]

    materia = Sucursales.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.direccion=direccion
    materia.telefono=telefono
    materia.correo=correo
    materia.horario=horario
    materia.encargado=encargado
    materia.save()
    return redirect('sucursal')

def borrarSucursal(request, codigo):
    materia=Sucursales.objects.get(codigo=codigo)
    materia.delete()
    return redirect('sucursal')