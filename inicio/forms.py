from django import forms


class PublicarPantalonForm(forms.Form):
    
    color = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    talle = forms.CharField(max_length=2)
    fecha_publicacion = forms.DateField(required=False)
    
class PublicarRemeraForm(forms.Form):
    
    color = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    talle = forms.CharField(max_length=2)
    fecha_publicacion= forms.DateField(required=False) 
    
    
class PublicarCalzadoForm(forms.Form):
    
    color = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=10)
    talle = forms.IntegerField()
    fecha_publicacion= forms.DateField(required=False) 
    
class BuscarPantalonForm(forms.Form):
    color = forms.CharField(max_length=15, required=False)
    
class BuscarRemeraForm(forms.Form):
    color = forms.CharField(max_length=15, required=False)
    
class BuscarCalzadoForm(forms.Form):
    color = forms.CharField(max_length=15, required=False)

