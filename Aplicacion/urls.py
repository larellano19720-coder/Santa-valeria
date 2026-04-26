from django.urls import path
from . import views


urlpatterns = [
     # Latido
     # Presentacion
     path('', views.menuInfo, name='Menu_Presentacion'),
     path('Sin_Servicio/', views.NoPago, name='SinServicio'),
    
]
