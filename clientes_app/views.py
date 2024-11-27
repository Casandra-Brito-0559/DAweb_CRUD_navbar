from django.shortcuts import render, redirect
from .models import Clientes
# Create your views here.
def inicio_vistaClientes(request):
    losclientes=Clientes.objects.all()
    return render(request, 'gestionCliente.html',{'misclientes':losclientes})
    
def registrarCliente(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    fecha = request.POST["datefecha"]

    guardarmateria = Clientes.objects.create(codigo=codigo,nombre=nombre,apellido=apellido,telefono=telefono,correo=correo,direccion=direccion,fecha=fecha)
    return redirect('cliente')

def seleccionarCliente(request, codigo):
    cliente = Clientes.objects.get(codigo=codigo)
    return render(request, 'editarCliente.html',{'misclientes':cliente})

def editarCliente(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    fecha = request.POST["datefecha"]

    materia = Clientes.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.apellido=apellido
    materia.telefono=telefono
    materia.correo=correo
    materia.direccion=direccion
    materia.fecha=fecha
    materia.save()
    return redirect('cliente')

def borrarCliente(request, codigo):
    materia=Clientes.objects.get(codigo=codigo)
    materia.delete()
    return redirect('cliente')