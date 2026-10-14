from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cantidad_min = models.IntegerField()
    cantidad_actual = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)