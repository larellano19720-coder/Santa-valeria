from django.shortcuts import render
from datetime import datetime, date
from django.utils import timezone
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from datetime import datetime, timedelta
from Aplicacion.views import servicioActivo

def FormularioSolicitudServido(request):
    ServiciosWeb = servicioActivo() 
    ultimo_contacto = tblRepartidor.objects.order_by('-ID').first()
    if ultimo_contacto:
        ultimo_folio = ultimo_contacto.ID + 1
    else:
        ultimo_folio = 1

    FECorrales = tblCorrales.objects.order_by('ID')
    FETolva = tblTolva.objects.exclude(ID=1).order_by('Alias')
    FEProductos = tblProductos.objects.all().exclude(ID=1).order_by('Descripcion')
    FEstatus = tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    FechaDeHoy = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')

    
    return render(request, 'SolicitudServido/form.html',{  'FECorrales': FECorrales, 'ultimo_folio':ultimo_folio, 'FETolva':FETolva,
    'FechaDeHoy':FechaDeHoy, 'FEstatus': FEstatus, 'FEProductos':FEProductos, 'ServiciosWeb':ServiciosWeb})

def FormularioReplicarServido(request):
    ServiciosWeb = servicioActivo() 
    ultimo_contacto = tblRepartidor.objects.order_by('-ID').first()
    if ultimo_contacto:
        ultimo_folio = ultimo_contacto.ID + 1
    else:
        ultimo_folio = 1
    if request.method == 'POST':
        fecha_str = request.POST.get('fecha')

        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")

        TEServidos = tblRepartidor.objects.filter(
            FechaSol__gte=fecha,
            FechaSol__lt=fecha + timedelta(minutes=2)
        ).values(
            'ID', 'Folio',
            'IDCorral_id__Descripcion',
            'IDCorral_id',
            'IDProducto_id__Descripcion',
            'IDEstatus_id__Descripcion',
            'IDProducto_id',
            'IDEstatus_id',
            'CantidadSolicitada',
            'CantidadAnimales',
            'SeSirve',
            'FechaSol',
            'FechaServida1'
        )
    registro = tblRepartidor.objects.filter(
            FechaSol__gte=fecha,
            FechaSol__lt=fecha + timedelta(minutes=2)
        ).first()
    porcentaje = registro.Porcentaje if registro else None
    FECorrales = tblCorrales.objects.order_by('ID')
    FETolva = tblTolva.objects.exclude(ID=1).order_by('Alias')
    FEProductos = tblProductos.objects.all().exclude(ID=1).order_by('Descripcion')
    FEstatus = tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    FechaDeHoy = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')

    
    return render(request, 'SolicitudServido/replicar.html',{  'FECorrales': FECorrales, 'ultimo_folio':ultimo_folio, 'FETolva':FETolva, 'porcentaje':porcentaje,
    'FechaDeHoy':FechaDeHoy, 'FEstatus': FEstatus, 'FEProductos':FEProductos, 'ServiciosWeb':ServiciosWeb, 'TEServidos':TEServidos})
    
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
