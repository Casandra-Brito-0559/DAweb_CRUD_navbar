from django.db import models

# Create your models here.

class Ventas(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    fecha = models.DateField()
    codigocli = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    codigolib = models.CharField(max_length=100)
    codigosu = models.CharField(max_length=100)
    codigoem = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
