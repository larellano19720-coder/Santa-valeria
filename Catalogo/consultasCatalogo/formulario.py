from django.shortcuts import render
from django.db.models import Q
from datetime import datetime
from django.utils import timezone
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from Aplicacion.views import servicioActivo

timezone.activate("America/Hermosillo")
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FORMUALRIO DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def FormualrioOperadores(request):
    ServiciosWeb = servicioActivo() 
    ultimo_id = tblOperadores.objects.order_by('-ID').first()
    if ultimo_id:
        ultimo_folio = ultimo_id.ID + 1
    else:
        ultimo_folio = 1
    
    FEstatus = tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    return render(request, 'Operador/form.html',{
    'FEstatus': FEstatus,'ultimo_folio': ultimo_folio, 'ServiciosWeb':ServiciosWeb})

def FormualrioMateriasPrimas(request):
    ServiciosWeb = servicioActivo() 
    ultimo_id = tblMateriaPrima.objects.order_by('-ID').first()
    if ultimo_id:
        ultimo_folio = ultimo_id.ID + 1
    else:
        ultimo_folio = 1
    
    FEstatus=tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    FUnidadMedida=tblUnidades.objects.all().order_by('Descripcion')
    return render(request, 'MateriaPrima/form.html',{
    'ultimo_folio': ultimo_folio, 'FEstatus': FEstatus, 'FUnidadMedida': FUnidadMedida, 'ServiciosWeb':ServiciosWeb})

def FormualrioProductos(request):
    ServiciosWeb = servicioActivo() 
    ultimo_id = tblProductos.objects.order_by('-ID').first()
    if ultimo_id:
        ultimo_folio = ultimo_id.ID + 1
    else:
        ultimo_folio = 1
    
    FEstatus=tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    FUnidadMedida=tblUnidades.objects.all().order_by('Descripcion')
    return render(request, 'Producto/form.html',{
    'ultimo_folio': ultimo_folio, 'FEstatus': FEstatus, 'FUnidadMedida': FUnidadMedida, 'ServiciosWeb':ServiciosWeb})

def FormualrioCorrales(request):
    ServiciosWeb = servicioActivo() 
    ultimo_id = tblCorrales.objects.order_by('-ID').first()
    if ultimo_id:
        ultimo_folio = ultimo_id.ID + 1
    else:
        ultimo_folio = 1
    FEstatus = tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    FechaDeHoy = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')
    
    return render(request, 'Corral/form.html',{
    'ultimo_folio': ultimo_folio, 'FechaDeHoy':FechaDeHoy, 'FEstatus': FEstatus, 'ServiciosWeb':ServiciosWeb})

def FormualrioTolva(request):
    ServiciosWeb = servicioActivo() 
    ultimo_id = tblTolva.objects.order_by('-ID').first()
    if ultimo_id:
        ultimo_folio = ultimo_id.ID + 1
    else:
        ultimo_folio = 1
    
    FUnidadMedida=tblUnidades.objects.all().order_by('Descripcion')
    FEstatus = tblEstatus.objects.filter(ID__gte=4, ID__lte=6).order_by('Descripcion')
    return render(request, 'Tolva/form.html',{
    'ultimo_folio': ultimo_folio,'FEstatus': FEstatus, 'FUnidadMedida': FUnidadMedida, 'ServiciosWeb':ServiciosWeb})