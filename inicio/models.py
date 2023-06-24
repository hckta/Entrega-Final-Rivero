from django.db import models

# Create your models here.
# En la descripcion del producto se podria agregar por ejemplo: 
# - La marca
# - Si el producto publicado es usado o nuevo
# - El tipo de prenda mas especifica: remera manga corta, manga larga; calzado zapatos,zapatillas,botines; pantalon largo, corto.

class Pantalon(models.Model):
    
    color = models.CharField(max_length=15)
    marca = models.CharField(max_length=10)
    talle = models.CharField(max_length=2)
    fecha_publicacion = models.DateField(null=True)
    
    
class Remera(models.Model):
    
    color = models.CharField(max_length=15)
    marca = models.CharField(max_length=10)
    talle = models.CharField(max_length=2)
    fecha_publicacion = models.DateField(null=True)
    
class Calzado(models.Model):
    
    color = models.CharField(max_length=15)
    marca = models.CharField(max_length=10)
    talle = models.IntegerField()
    fecha_publicacion = models.DateField(null=True)
