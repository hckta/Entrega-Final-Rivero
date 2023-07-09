from django.db import models
from django.forms.widgets import DateInput
from ckeditor.fields import RichTextField

# Create your models here.
# En la descripcion del producto se podria agregar por ejemplo: 
# - Si el producto publicado es usado o nuevo
# - El tipo de prenda mas especifica: remera manga corta, manga larga; calzado zapatos,zapatillas,botines; pantalon largo, corto.

class Pantalon(models.Model):
    
    color = models.CharField(max_length=15)
    marca = models.CharField(max_length=10)
    talle = models.CharField(max_length=2)
    descripcion = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='pantalones',blank=True, null=True)
    fecha_publicacion = models.DateField(blank=True, null=True)
        
    
class Remera(models.Model):
    
    color = models.CharField(max_length=15)
    marca = models.CharField(max_length=10)
    talle = models.CharField(max_length=2)
    descripcion = RichTextField(null=True)
    imagen = models.ImageField(upload_to='remeras',blank=True, null=True)
    fecha_publicacion = models.DateField(null=True)
    
class Calzado(models.Model):
    
    color = models.CharField(max_length=15)
    marca = models.CharField(max_length=10)
    talle = models.IntegerField()
    descripcion = RichTextField(null=True)
    imagen = models.ImageField(upload_to='calzados',blank=True, null=True)
    fecha_publicacion = models.DateField(null=True)
