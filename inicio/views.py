from django.shortcuts import render
from inicio.forms import PublicarPantalonForm, PublicarRemeraForm, PublicarCalzadoForm
from inicio.models import Pantalon, Remera, Calzado
# Create your views here.


def inicio(request):
    return render(request, 'inicio/inicio.html')

def publicar_pantalon(request):
    mensaje = ''
    if request.method == 'POST':
        formulario = PublicarPantalonForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            pantalon = Pantalon(color=info['color'],marca=info['marca'],talle=info['talle'],fecha_publicacion=info['fecha_publicacion'])
            pantalon.save()
            mensaje ='Se publico el pantalon exitosamente' 
        else:
            return render(request,'inicio/publicar_pantalon.html', {'formulario':formulario}) 
    
    formulario = PublicarPantalonForm()
    return render(request,'inicio/publicar_pantalon.html', {'formulario':formulario, 'mensaje': mensaje})
    
    
def publicar_remera(request):
    mensaje = ''
    if request.method == 'POST':
        formulario = PublicarRemeraForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            remera = Remera(color=info['color'],marca=info['marca'],talle=info['talle'],fecha_publicacion=info['fecha_publicacion'])
            remera.save()
            mensaje ='Se publico la remera exitosamente'
        else:
            return render(request,'inicio/publicar_remera.html', {'formulario':formulario})
    
    formulario = PublicarRemeraForm()
    return render(request,'inicio/publicar_remera.html', {'formulario':formulario, 'mensaje': mensaje})
    
    
def publicar_calzado(request):
    mensaje = ''
    if request.method == 'POST':
        formulario = PublicarCalzadoForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            calzado = Calzado(color=info['color'],marca=info['marca'],talle=info['talle'],fecha_publicacion=info['fecha_publicacion'])
            calzado.save()
            mensaje ='Se publico el calzado exitosamente'
        else:
            return render(request,'inicio/publicar_calzado.html',{'formulario':formulario})
            
    formulario = PublicarCalzadoForm()
    return render(request,'inicio/publicar_calzado.html',{'formulario':formulario, 'mensaje': mensaje})
    

