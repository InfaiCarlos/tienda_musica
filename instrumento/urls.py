from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_instrumentos, name='listar_instrumentos'),
    path('crear/', views.crear_instrumento, name='crear_instrumento'),
    path('editar/<int:id>/', views.editar_instrumento, name='editar_instrumento'),
    path('eliminar/<int:id>/', views.eliminar_instrumento, name='eliminar_instrumento'),
]

