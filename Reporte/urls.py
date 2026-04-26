from django.urls import path
from . import views

from Reporte.ConsultasReportes import reporte

urlpatterns = [
    path('Reporte_Movimiento_Servidos/', reporte.reporteServidosMovimientos, name='T_Reporte'),
]
