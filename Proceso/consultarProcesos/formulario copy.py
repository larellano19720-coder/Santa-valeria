from django.shortcuts import render
from datetime import datetime, date
from django.utils import timezone
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Q
from Aplicacion.views import servicioActivo
def FormularioSolicitudServido(request):
    ServiciosWeb = servicioActivo() 
    ultimo_contacto = tblRepartidor.objects.order_by('-ID').first()
    if ultimo_contacto:
        ultimo_folio = ultimo_contacto.ID + 1
    else:
        ultimo_folio = 1

    FECorrales = tblCorrales.objects.order_by('Descripcion')
    FETolva = tblTolva.objects.order_by('Alias')
    FEProductos = tblProductos.objects.all().exclude(ID=1).order_by('Descripcion')
    FEstatus = tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    FechaDeHoy = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')

    
    return render(request, 'SolicitudServido/form.html',{  'FECorrales': FECorrales, 'ultimo_folio':ultimo_folio, 'FETolva':Proceso/consultarProcesos/formulario.py,
    'FechaDeHoy':FechaDeHoy, 'FEstatus': FEstatus, 'FEProductos':FEProductos, 'ServiciosWeb':ServiciosWeb})

def FormularioServidoAnimales(request):
    ServiciosWeb = servicioActivo() 
    ultimo_contacto = tblRepartidor.objects.order_by('-ID').first()
    if ultimo_contacto:
        ultimo_folio = ultimo_contacto.ID + 1
    else:
        ultimo_folio = 1
    FECorrales = tblCorrales.objects.all().order_by('Descripcion')
    FEProductos = tblProductos.objects.all().exclude(ID=1).order_by('Descripcion')
    FEstatus = tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    FechaDeHoy = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')
    
    
    return render(request, 'Procesos/Servido Manual/form.html',{  'FECorrales': FECorrales, 'ultimo_folio':ultimo_folio,
    'FechaDeHoy':FechaDeHoy,  'FEstatus': FEstatus, 'FEProductos':FEProductos, 'ServiciosWeb':ServiciosWeb})
