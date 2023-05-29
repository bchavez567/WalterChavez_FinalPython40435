from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre= models.CharField(max_length=40)
    precio= models.IntegerField()

class Contacto(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Libros(models.Model):
    nombre= models.CharField(max_length=30)
    imagen= models.ImageField()
    url = models.CharField(max_length=130)
    def __str__(self):
        return f"Nombre: {self.nombre} - Imagen: {self.imagen} Url {self.url}"