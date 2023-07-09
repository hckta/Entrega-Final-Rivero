from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from usuario.form import MiCrearUsuariosForm, MiEditarUsuariosForm
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuario.models import InfoExtra
from django.views.generic import TemplateView
# Create your views here.

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            user = authenticate(username=usuario, password=contrasenia)
            
            django_login(request,user)
            
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuario/login.html', {'formulario': formulario})
    
    
    formulario = AuthenticationForm()
    return render(request, 'usuario/login.html', {'formulario': formulario})


def registrarse(request):
    
    if request.method == 'POST':
        formulario = MiCrearUsuariosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuario:login')
        else:
            return render(request, 'usuario/registro.html', {'formulario': formulario})
            
    formulario = MiCrearUsuariosForm()
    return render(request, 'usuario/registro.html', {'formulario': formulario})


class MostrarPerfil(LoginRequiredMixin, DetailView):
    model = User
    template_name = "usuario/CBV/perfil_CBV.html"
    context_object_name = 'usuario'
    

    
@login_required
def editar_perfil(request):
    info_extra_user = request.user.infoextra
    if request.method == 'POST':
        formulario = MiEditarUsuariosForm(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            avatar = formulario.cleaned_data.get('avatar')
            descripcion = formulario.cleaned_data.get('descripcion')
            link_web = formulario.cleaned_data.get('link_web')
            if avatar:
                info_extra_user.avatar = avatar
            if descripcion:
                info_extra_user.descripcion = descripcion
            if link_web:
                info_extra_user.link_web = link_web
                
            info_extra_user.save()
            formulario.save()
            return redirect('inicio:inicio')   
    else:    
        formulario = MiEditarUsuariosForm(initial= {'avatar': info_extra_user.avatar,'descripcion': info_extra_user.descripcion, 'link_web': info_extra_user.link_web}, instance=request.user)
        
    return render(request, 'usuario/editar_perfil.html', {'formulario': formulario})


class ModificarPass(LoginRequiredMixin,PasswordChangeView):
    template_name = 'usuario/modificar_pass.html'
    success_url = reverse_lazy('usuario:editar_perfil')
    
    
class AcercaDeMi(LoginRequiredMixin, TemplateView):
    model = User
    template_name = "usuario/acerca_de_mi.html"
    context_object_name = 'usuario'
    