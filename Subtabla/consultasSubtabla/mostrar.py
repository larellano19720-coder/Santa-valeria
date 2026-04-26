from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from Aplicacion.views import servicioActivo
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------ESTATUS---------------------------------------------------------
def TablaEstatus(request):
    ServiciosWeb = servicioActivo() 
    TEstatus = tblEstatus.objects.all()
    return render(request, 'Estatus/index.html',{
    'TEstatus': TEstatus, 'ServiciosWeb':ServiciosWeb})

def TablaUnidadMedida(request):
    ServiciosWeb = servicioActivo() 
    TUnidadMedida = tblUnidades.objects.all()
    return render(request, 'UnidadMedida/index.html',{
    'TUnidadMedida': TUnidadMedida, 'ServiciosWeb':ServiciosWeb})
