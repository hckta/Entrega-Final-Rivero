from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('pantalon/publicar/', views.publicar_pantalon, name ='publicar_pantalon'),
    path('remera/publicar/', views.publicar_remera, name ='publicar_remera'),
    path('calzado/publicar/', views.publicar_calzado, name ='publicar_calzado'),
    path('pantalones/', views.listar_pantalones, name='listar_pantalones'),
    path('remeras/', views.listar_remeras, name='listar_remeras'),
    path('calzados/', views.listar_calzados, name='listar_calzados'),

]
