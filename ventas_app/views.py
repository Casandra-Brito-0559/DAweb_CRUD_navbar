from django.shortcuts import render, redirect
from .models import Ventas
# Create your views here.
def inicio_vistaVentas(request):
    losventas=Ventas.objects.all()
    return render(request, 'gestionVenta.html',{'misventas':losventas})
    
def registrarVenta(request):
    codigo = request.POST["txtcodigo"]
    fecha = request.POST["datefecha"]
    codigocli = request.POST["txtcodigocli"]
    cantidad = request.POST["numcantidad"]
    codigolib = request.POST["txtcodigolib"]
    codigisu = request.POST["txtcodigosu"]
    codigoem = request.POST["txtcodigoem"]
    
    

    guardarmateria = Ventas.objects.create(codigo=codigo,fecha=fecha,codigocli=codigocli,cantidad=cantidad,codigolib=codigolib,codigosu=codigisu,codigoem=codigoem)
    return redirect('venta')

def seleccionarVenta(request, codigo):
    venta = Ventas.objects.get(codigo=codigo)
    return render(request, 'editarVenta.html',{'misventas':Ventas})

def editarVenta(request):
    codigo = request.POST["txtcodigo"]
    fecha = request.POST["datefecha"]
    codigocli = request.POST["txtcodigocli"]
    cantidad = request.POST["numcantidad"]
    codigolib = request.POST["txtcodigolib"]
    codigisu = request.POST["txtcodigosu"]
    codigoem = request.POST["txtcodigoem"]

    materia = Ventas.objects.get(codigo=codigo)
    materia.fecha=fecha
    materia.codigocli=codigocli 
    materia.codigolib=codigolib
    materia.cantidad=cantidad
    materia.codigosu=codigisu
    materia.codigoem=codigoem
    
    materia.save()
    return redirect('venta')

def borrarVenta(request, codigo):
    materia=Ventas.objects.get(codigo=codigo)
    materia.delete()
    return redirect("venta")
