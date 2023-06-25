from django.shortcuts import render, redirect
from inicio.forms import PublicarPantalonForm, PublicarRemeraForm, PublicarCalzadoForm, BuscarPantalonForm, BuscarRemeraForm, BuscarCalzadoForm
from inicio.models import Pantalon, Remera, Calzado
# Create your views here.


def inicio(request):
    return render(request, 'inicio/inicio.html')

def publicar_pantalon(request):
    if request.method == 'POST':
        formulario = PublicarPantalonForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            pantalon = Pantalon(color=info['color'],marca=info['marca'],talle=info['talle'],fecha_publicacion=info['fecha_publicacion'])
            pantalon.save()
            return redirect('inicio:listar_pantalones',) 
        else:
            return render(request,'inicio/publicar_pantalon.html', {'formulario':formulario}) 
    
    formulario = PublicarPantalonForm()
    return render(request,'inicio/publicar_pantalon.html', {'formulario':formulario})
    
    
def publicar_remera(request):
    if request.method == 'POST':
        formulario = PublicarRemeraForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            remera = Remera(color=info['color'],marca=info['marca'],talle=info['talle'],fecha_publicacion=info['fecha_publicacion'])
            remera.save()
            return redirect('inicio:listar_remeras') 
        else:
            return render(request,'inicio/publicar_remera.html', {'formulario':formulario})
    
    formulario = PublicarRemeraForm()
    return render(request,'inicio/publicar_remera.html', {'formulario':formulario})
    
    
def publicar_calzado(request):
    if request.method == 'POST':
        formulario = PublicarCalzadoForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            calzado = Calzado(color=info['color'],marca=info['marca'],talle=info['talle'],fecha_publicacion=info['fecha_publicacion'])
            calzado.save()
            return redirect('inicio:listar_calzados')  
        else:
            return render(request,'inicio/publicar_calzado.html',{'formulario':formulario})
            
    formulario = PublicarCalzadoForm()
    return render(request,'inicio/publicar_calzado.html',{'formulario':formulario})

def listar_pantalones(request):
    formulario = BuscarPantalonForm(request.GET)
    if formulario.is_valid():
        color_buscado = formulario.cleaned_data['color']
        listado_pantalones = Pantalon.objects.filter(color__icontains=color_buscado)
        
    formulario = BuscarPantalonForm()
    return render(request,'inicio/listar_pantalones.html',{'formulario':formulario, 'pantalones':listado_pantalones})

def listar_remeras(request):
    formulario = BuscarRemeraForm(request.GET)
    if formulario.is_valid():
        color_buscado = formulario.cleaned_data['color']
        listado_remeras = Remera.objects.filter(color__icontains=color_buscado)
        
    formulario = BuscarRemeraForm()
    return render(request,'inicio/listar_remeras.html',{'formulario':formulario, 'remeras':listado_remeras})

def listar_calzados(request):
    formulario = BuscarCalzadoForm(request.GET)
    if formulario.is_valid():
        color_buscado = formulario.cleaned_data['color']
        listado_calzado = Calzado.objects.filter(color__icontains=color_buscado)
        
    formulario = BuscarCalzadoForm()    
    return render(request,'inicio/listar_calzados.html',{'formulario':formulario, 'calzados':listado_calzado} )
