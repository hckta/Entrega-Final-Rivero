from django.shortcuts import render, redirect
from inicio.forms import PublicarPantalonForm, PublicarRemeraForm, PublicarCalzadoForm, BuscarPantalonForm, BuscarRemeraForm, BuscarCalzadoForm, ModificarPantalonForm, ModificarRemeraForm, ModificarCalzadoForm
from inicio.models import Pantalon, Remera, Calzado
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from django.urls import reverse_lazy
# Create your views here.


def inicio(request):
    return render(request, 'inicio/inicio.html')

#Vistas de Publicado

# @login_required
# def publicar_pantalon(request):
#     if request.method == 'POST':
#         formulario = PublicarPantalonForm(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             pantalon = Pantalon(color=info['color'],marca=info['marca'],talle=info['talle'],descripcion=info['descripcion'],fecha_publicacion=info['fecha_publicacion'])
#             pantalon.save()
#             return redirect('inicio:listar_pantalones',) 
#         else:
#             return render(request,'inicio/publicar_pantalon.html', {'formulario':formulario}) 
    
#     formulario = PublicarPantalonForm()
#     return render(request,'inicio/publicar_pantalon.html', {'formulario':formulario})
    
@login_required    
def publicar_remera(request):
    if request.method == 'POST':
        formulario = PublicarRemeraForm(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            remera = Remera(color=info['color'],marca=info['marca'],talle=info['talle'],descripcion=info['descripcion'],imagen = info['imagen'],fecha_publicacion=info['fecha_publicacion'])
            remera.save()
            return redirect('inicio:listar_remeras') 
        else:
            return render(request,'inicio/publicar_remera.html', {'formulario':formulario})
    
    formulario = PublicarRemeraForm()
    return render(request,'inicio/publicar_remera.html', {'formulario':formulario})
    
@login_required    
def publicar_calzado(request):
    if request.method == 'POST':
        formulario = PublicarCalzadoForm(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            calzado = Calzado(color=info['color'],marca=info['marca'],talle=info['talle'],descripcion=info['descripcion'],imagen = info['imagen'],fecha_publicacion=info['fecha_publicacion'])
            calzado.save()
            return redirect('inicio:listar_calzados')  
        else:
            return render(request,'inicio/publicar_calzado.html',{'formulario':formulario})
            
    formulario = PublicarCalzadoForm()
    return render(request,'inicio/publicar_calzado.html',{'formulario':formulario})

#Vistas de listados
@login_required
def listar_pantalones(request):
    formulario = BuscarPantalonForm(request.GET)
    if formulario.is_valid():
        color_buscado = formulario.cleaned_data['color']
        listado_pantalones = Pantalon.objects.filter(color__icontains=color_buscado)
        
    formulario = BuscarPantalonForm()
    return render(request,'inicio/listar_pantalones.html',{'formulario':formulario, 'pantalones':listado_pantalones})

@login_required
def listar_remeras(request):
    formulario = BuscarRemeraForm(request.GET)
    if formulario.is_valid():
        color_buscado = formulario.cleaned_data['color']
        listado_remeras = Remera.objects.filter(color__icontains=color_buscado)
        
    formulario = BuscarRemeraForm()
    return render(request,'inicio/listar_remeras.html',{'formulario':formulario, 'remeras':listado_remeras})

@login_required
def listar_calzados(request):
    formulario = BuscarCalzadoForm(request.GET)
    if formulario.is_valid():
        color_buscado = formulario.cleaned_data['color']
        listado_calzado = Calzado.objects.filter(color__icontains=color_buscado)
        
    formulario = BuscarCalzadoForm()    
    return render(request,'inicio/listar_calzados.html',{'formulario':formulario, 'calzados':listado_calzado} )

#Vistas para eliminar

@login_required
def eliminar_pantalon(request, pantalon_id):
    pantalon = Pantalon.objects.get(id=pantalon_id)
    pantalon.delete()
    
    return redirect('inicio:listar_pantalones')

@login_required    
def eliminar_remera(request, remera_id):
    remera = Remera.objects.get(id=remera_id)
    remera.delete()
    return redirect('inicio:listar_remeras')

@login_required    
def eliminar_calzado(request, calzado_id):
    calzado = Calzado.objects.get(id=calzado_id)
    calzado.delete()
    return redirect('inicio:listar_calzados')

#Vistas de modificar
# @login_required
# def modificar_pantalon(request, pantalon_id):
#     pantalon_a_modificar = Pantalon.objects.get(id=pantalon_id)
    
#     if request.method == 'POST':
#         formulario = ModificarPantalonForm(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             pantalon_a_modificar.color = info['color']
#             pantalon_a_modificar.marca = info['marca']
#             pantalon_a_modificar.talle = info['talle']
#             pantalon_a_modificar.descripcion = info['descripcion']
#             pantalon_a_modificar.save()
#             return redirect('inicio:listar_pantalones')
#         else:
#             return render(request, 'inicio/modificar_pantalon.html', {'formulario': formulario})
#     formulario = ModificarPantalonForm(initial={'color': pantalon_a_modificar.color, 'marca': pantalon_a_modificar.marca, 'talle': pantalon_a_modificar.talle, 'descripcion': pantalon_a_modificar.descripcion})
#     return render(request, 'inicio/modificar_pantalon.html', {'formulario': formulario})

@login_required 
def modificar_remera(request, remera_id):
    remera_a_modificar = Remera.objects.get(id=remera_id)
    
    if request.method == 'POST':
        formulario = ModificarRemeraForm(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            remera_a_modificar.color = info['color']
            remera_a_modificar.marca = info['marca']
            remera_a_modificar.talle = info['talle']
            remera_a_modificar.descripcion = info['descripcion']
            remera_a_modificar.imagen = info['imagen']
            remera_a_modificar.save()
            return redirect('inicio:listar_remeras')
        else:
            return render(request, 'inicio/modificar_remera.html', {'formulario': formulario})
    formulario = ModificarRemeraForm(initial={'color': remera_a_modificar.color, 'marca': remera_a_modificar.marca, 'talle': remera_a_modificar.talle, 'descripcion': remera_a_modificar.descripcion, 'imagen': remera_a_modificar.imagen})
    return render(request, 'inicio/modificar_remera.html', {'formulario': formulario})

# @login_required    
# def modificar_calzado(request, calzado_id):
#     calzado_a_modificar = Calzado.objects.get(id=calzado_id)
    
#     if request.method == 'POST':
#         formulario = ModificarCalzadoForm(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             calzado_a_modificar.color = info['color']
#             calzado_a_modificar.marca = info['marca']
#             calzado_a_modificar.talle = info['talle']
#             calzado_a_modificar.descripcion = info['descripcion']
#             calzado_a_modificar.save()
#             return redirect('inicio:listar_calzados')
#         else:
#             return render(request, 'inicio/modificar_calzado.html', {'formulario': formulario})
#     formulario = ModificarCalzadoForm(initial={'color': calzado_a_modificar.color, 'marca': calzado_a_modificar.marca, 'talle': calzado_a_modificar.talle, 'descripcion': calzado_a_modificar.descripcion})
#     return render(request, 'inicio/modificar_calzado.html', {'formulario': formulario})


# Mostrar descripciones con Clase Basada en Vistas

class MostrarPantalon(LoginRequiredMixin,DetailView):
    model = Pantalon
    template_name = "inicio/CBV/mostrar_pantalon_CBV.html"
    
class MostrarRemera(LoginRequiredMixin,DetailView):
    model = Remera
    template_name = "inicio/CBV/mostrar_remera_CBV.html"
    
class MostrarCalzado(LoginRequiredMixin,DetailView):
    model = Calzado
    template_name = "inicio/CBV/mostrar_calzado_CBV.html"
    
#Tuve que cambiar las vistas hechas como funciones por CBV porque sino no podia usar la texto enriquecido en las descripciones :)
    
    
class PublicarPantalon(LoginRequiredMixin,CreateView):
    model = Pantalon
    template_name = 'inicio/CBV/publicar_pantalon_CBV.html'
    fields = ['color', 'marca', 'talle', 'descripcion','fecha_publicacion', 'imagen']
    success_url = reverse_lazy('inicio:listar_pantalones')
    
# Decidi, en este caso, usar una vista como funcion para poder mostrar el uso de Datefield con el calendario en el campo fecha_publicacion.
# Esto se debe a que solo supe usar el calendario con las vistas de funciones y no con las CBV

# class PublicarRemera(CreateView):
#     model = Remera
#     template_name = 'inicio/CBV/publicar_remera_CBV.html'
#     fields = ['color', 'marca', 'talle', 'descripcion', 'fecha_publicacion']
#     success_url = reverse_lazy('inicio:listar_remeras')
    
class PublicarCalzado(LoginRequiredMixin, CreateView):
    model = Calzado
    template_name = 'inicio/CBV/publicar_calzado_CBV.html'
    fields = ['color', 'marca', 'talle', 'descripcion', 'fecha_publicacion', 'imagen']
    success_url = reverse_lazy('inicio:listar_calzados')
    

class ModificarPantalon(LoginRequiredMixin, UpdateView):
    model = Pantalon
    template_name = 'inicio/CBV/modificar_pantalon_CBV.html'
    fields = ['color', 'marca', 'talle', 'descripcion', 'imagen']
    success_url = reverse_lazy('inicio:listar_pantalones')
    
#Esta vista no esta activa, no se usara ya que en esta se usara el calendario para introducir la fecha
# class ModificarRemera(LoginRequiredMixin, UpdateView):
#     model = Remera
#     template_name = 'inicio/CBV/modificar_remera_CBV.html'
#     fields = ['color', 'marca', 'talle', 'descripcion', 'fecha_publicacion']
#     success_url = reverse_lazy('inicio:listar_remeras')
    
class ModificarCalzado(LoginRequiredMixin, UpdateView):
    model = Calzado
    template_name = 'inicio/CBV/modificar_calzado_CBV.html'
    fields = ['color', 'marca', 'talle', 'descripcion', 'imagen']
    success_url = reverse_lazy('inicio:listar_calzados')
    
class CargarImagenes(LoginRequiredMixin,ListView):
    ...
    
    
    
    


