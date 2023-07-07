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
    path('pantalon/eliminar/<int:pantalon_id>/', views.eliminar_pantalon, name='eliminar_pantalon'),
    path('remera/eliminar/<int:remera_id>/', views.eliminar_remera, name='eliminar_remera'),
    path('calzado/eliminar/<int:calzado_id>/', views.eliminar_calzado, name='eliminar_calzado'),
    path('pantalon/modificar/<int:pantalon_id>/', views.modificar_pantalon, name='modificar_pantalon'),
    path('remera/modificar/<int:remera_id>/', views.modificar_remera, name='modificar_remera'),
    path('calzado/modificar/<int:calzado_id>/', views.modificar_calzado, name='modificar_calzado'),
    path('pantalon/mostrar/<int:pk>/', views.MostrarPantalon.as_view(), name='mostrar_pantalon'),
    path('remera/mostrar/<int:pk>/', views.MostrarRemera.as_view(), name='mostrar_remera'),
    path('calzado/mostrar/<int:pk>/', views.MostrarCalzado.as_view(), name='mostrar_calzado'),

]
