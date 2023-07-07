from django import forms
from django.forms.widgets import DateInput
from datetime import date

#Formularios de Publicacion


class PublicarPantalonForm(forms.Form):
    
    color = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    talle = forms.CharField(max_length=2)
    fecha_publicacion = forms.DateField(required=False, widget=DateInput (attrs={'type': 'date'}))
    
class PublicarRemeraForm(forms.Form):
    
    color = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    talle = forms.CharField(max_length=2)
    fecha_publicacion = forms.DateField(required=False, widget=DateInput (attrs={'type': 'date'}))
    
    
class PublicarCalzadoForm(forms.Form):
    
    color = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    talle = forms.IntegerField()
    fecha_publicacion = forms.DateField(required=False, widget=DateInput (attrs={'type': 'date'}))
    
#Formularios de Busqueda
    
class BuscarPantalonForm(forms.Form):
    color = forms.CharField(max_length=15, required=False)
    
class BuscarRemeraForm(forms.Form):
    color = forms.CharField(max_length=15, required=False)
    
class BuscarCalzadoForm(forms.Form):
    color = forms.CharField(max_length=15, required=False)
    
#Formularios de Modificacion

class ModificarPantalonForm(forms.Form):
    color = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    talle = forms.CharField(max_length=2)
    ...
    
class ModificarRemeraForm(ModificarPantalonForm):
    ...
    
class ModificarCalzadoForm(ModificarPantalonForm):
    talle = forms.IntegerField()
    ...
    
