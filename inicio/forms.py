from django import forms
from django.forms.widgets import DateInput
from datetime import date
from ckeditor.fields import RichTextField

#Formularios de Publicacion


class PublicarPantalonForm(forms.Form):
    
    color = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    talle = forms.CharField(max_length=2)
    descripcion = forms.CharField(required=False, max_length=20)
    imagen = forms.ImageField(required=False)
    # fecha_publicacion = forms.DateField(required=False, widget=DateInput(attrs={'type': 'date'}))
    
class PublicarRemeraForm(forms.Form):
    
    color = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    talle = forms.CharField(max_length=2)
    descripcion = forms.CharField(max_length=100)
    imagen = forms.ImageField(required=False)
    fecha_publicacion = forms.DateField(required=False, widget=DateInput (attrs={'type': 'date'}))
    
    
class PublicarCalzadoForm(forms.Form):
    
    color = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    talle = forms.IntegerField()
    descripcion = forms.CharField(max_length=100)
    imagen = forms.ImageField(required=False)
    # fecha_publicacion = forms.DateField(required=False, widget=DateInput (attrs={'type': 'date'}))
    
#Formularios de Busqueda
    
class BuscarPantalonForm(forms.Form):
    color = forms.CharField(max_length=15, required=False)
    
class BuscarRemeraForm(forms.Form):
    color = forms.CharField(max_length=15, required=False)
    
class BuscarCalzadoForm(forms.Form):
    color = forms.CharField(max_length=15, required=False)
    
#Formularios de Modificacion
#Esta vez use que los formularios hereden del formulario padre

class ModificarPantalonForm(forms.Form):
    color = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    talle = forms.CharField(max_length=2)
    descripcion = forms.CharField(max_length=100)
    imagen = forms.ImageField(required=False)
    # fecha_publicacion = forms.DateField(required=False, widget=DateInput (attrs={'type': 'date'}))
    ...
    
class ModificarRemeraForm(ModificarPantalonForm):
    imagen = forms.ImageField(required=False)
    ...
    
class ModificarCalzadoForm(ModificarPantalonForm):
    imagen = forms.ImageField(required=False)
    descripcion = RichTextField()
    talle = forms.IntegerField()
    ...
    
