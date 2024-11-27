from django.db import models

# Create your models here.

class Libros(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    presio = models.CharField(max_length=1000)
    cantidad = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre