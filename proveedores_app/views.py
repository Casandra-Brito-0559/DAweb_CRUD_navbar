from django.shortcuts import render, redirect
from .models import Proveedores
# Create your views here.
def inicio_vistaProveedor(request):
    losproveedores=Proveedores.objects.all()
    return render(request, 'gestionProveedor.html',{'misproveedores':losproveedores})
    
def registrarProveedor(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    gerente = request.POST["txtgerente"]
    cantidad = request.POST["numcantidad"]
    fecha = request.POST["datefecha"]

    guardarmateria = Proveedores.objects.create(codigo=codigo,nombre=nombre,telefono=telefono,correo=correo,gerente=gerente,cantidad=cantidad,fecha=fecha)
    return redirect('proveedor')

def seleccionarProveedor(request, codigo):
    proveedor = Proveedores.objects.get(codigo=codigo)
    return render(request, 'editarProveedor.html',{'misproveedores':proveedor})

def editarProveedor(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    gerente = request.POST["txtgerente"]
    cantidad = request.POST["numcantidad"]
    fecha = request.POST["datefecha"]

    materia = Proveedores.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.telefono=telefono
    materia.correo=correo
    materia.gerente=gerente
    materia.cantidad=cantidad
    materia.fecha=fecha
    materia.save()
    return redirect('proveedor')

def borrarProveedor(request, codigo):
    materia=Proveedores.objects.get(codigo=codigo)
    materia.delete()
    return redirect("proveedor")