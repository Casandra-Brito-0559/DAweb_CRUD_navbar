from django.db import models

# Create your models here.

class Autores(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    librose = models.IntegerField()
    contacto = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    popularidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre