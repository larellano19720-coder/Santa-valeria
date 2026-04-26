from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum
from django.db.models import Q
from datetime import datetime, timedelta
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum, Count, Q, Max
from django.db.models.functions import TruncDate
from django.db.models import F, FloatField, ExpressionWrapper, Value
from Aplicacion.views import servicioActivo
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE PROCESOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# -------------------------------------------------SERVIDOS ANIMALES---------------------------------------------------
def TablaSolicitudServido(request):
    ServiciosWeb = servicioActivo() 
    TGServidos = (
        tblRepartidor.objects
        .filter(Q(IDEstatus_id=3) | Q(IDEstatus_id=8) | Q(IDEstatus_id=13))
        .annotate(fecha=TruncDate('FechaSol'))
        .values('FechaSol')
        .annotate(
            total_cantidad=Sum('CantidadSolicitada'),
            total_registros=Count('ID'),
            total_estatus3=Count('ID', filter=Q(SeSirve="Si")),
            productos_distintos=Count('IDProducto_id', distinct=True),
            porcentaje=Max('Porcentaje'),
            estatus=Max('IDEstatus_id__Descripcion'),
            idestatus=Max('IDEstatus_id'),
            ids=Max('ID')
        )
        .order_by('-FechaSol')
    )

    TFServidos = tblRepartidor.objects.filter(IDEstatus_id=13).annotate(fecha=TruncDate('FechaSol')).values('FechaSol').first()
    THServidos = (
        tblRepartidor.objects
        .filter( Q(IDEstatus_id=10))
        .annotate(fecha=TruncDate('FechaSol'))
        .values('FechaSol')
        .annotate(
            total_cantidad=Sum('CantidadSolicitada'),
            total_servido = Sum(F('Cantidad1') + F('Cantidad2')),
            total_registros=Count('ID'),
            total_estatus3=Count('ID', filter=Q(SeSirve="Si")),
            productos_distintos=Count('IDProducto_id', distinct=True),
            porcentaje=Max('Porcentaje'),
            estatus=Max('IDEstatus_id__Descripcion'),
            idestatus=Max('IDEstatus_id')
        )
        .order_by('-FechaSol')[:5]
    )
    return render(request, 'SolicitudServido/index.html',{'THServidos': THServidos, 'TGServidos':TGServidos, 'ServiciosWeb':ServiciosWeb, 'TFServidos':TFServidos})

def TablaOrdenesServido(request):
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
        ).annotate(
        calcCantidad1=ExpressionWrapper(
            F('CantidadSolicitada') * F('Porcentaje') / 100,
            output_field=FloatField()
        ),
        calcCantidad2=ExpressionWrapper(
            F('CantidadSolicitada') - (F('CantidadSolicitada') * F('Porcentaje') / 100),
            output_field=FloatField()
        ),
        calcSuma=ExpressionWrapper(
            F('Cantidad1') + F('Cantidad2'),
            output_field=FloatField()
        )
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
            'calcCantidad1',
            'calcCantidad2',  
            'calcSuma',                 
            'Cantidad1',
            'Cantidad2',                       
            'SeSirve',
            'FechaSol',
            'FechaServida1',
            'FechaServida2'
            
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

    
    return render(request, 'SolicitudServido/mostrar.html',{  'FECorrales': FECorrales, 'ultimo_folio':ultimo_folio, 'FETolva':FETolva, 'porcentaje':porcentaje,
    'FechaDeHoy':FechaDeHoy, 'FEstatus': FEstatus, 'FEProductos':FEProductos, 'ServiciosWeb':ServiciosWeb, 'TEServidos':TEServidos})
    
def TablaServidoCorral(request):
    ServiciosWeb = servicioActivo() 
    FechaDeHoy = timezone.localtime(timezone.now()).strftime('%Y-%m-%d')
    TServidos = tblRepartidor.objects.filter(Q(IDEstatus_id = 10) | Q(IDEstatus_id = 11)).values('ID', 'Folio',
    'IDCorral_id__Descripcion','IDProducto_id__Descripcion','IDEstatus_id__Descripcion',
    'CantidadSolicitada',  'FechaSol', 'FechaServida1'
    )
    
    return render(request, 'ServidoListo/index.html',{'FechaDeHoy':FechaDeHoy, 'TServidos': TServidos, 'ServiciosWeb':ServiciosWeb })


def TablaServidoManual(request):
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

    
    return render(request, 'ServidoManual/index.html',{  'FECorrales': FECorrales, 'ultimo_folio':ultimo_folio, 'FETolva':FETolva, 'porcentaje':porcentaje,
    'FechaDeHoy':FechaDeHoy, 'FEstatus': FEstatus, 'FEProductos':FEProductos, 'ServiciosWeb':ServiciosWeb, 'TEServidos':TEServidos})



def TablaCargamentoTolva(request):
    ServiciosWeb = servicioActivo()
    TTolva = tblTolva.objects.exclude(ID=1).values('ID', 'Alias', 'IDProducto_id__Descripcion', 'IDEstatus_id__Descripcion', 'IDEstatus_id', 'IDProducto_id')
    TServido = tblRepartidor.objects.filter(IDEstatus = 8).values('ID', 'Folio',
    'IDCorral_id__Descripcion','IDProducto_id','IDEstatus_id__Descripcion',
    'CantidadSolicitada', 'FechaSol', 'IDTolva_id'
    )
    TFormulado = tblFormulado.objects.filter(IDEstatus = 8).values('ID', 'Folio', 'IDEstatus_id',
    'IDMateriaPrima__Descripcion','IDProducto_id','IDProducto_id__Descripcion','IDEstatus_id__Descripcion',
    'CantidadSolicitada'
    )
    return render(request, 'TolvaProcesos/index.html',{'TTolva': TTolva, 'TServido':TServido, 'TFormulado':TFormulado, 'ServiciosWeb':ServiciosWeb })


    ServiciosWeb = servicioActivo()
    producto = request.POST.get('producto', '')
    tolva = request.POST.get('tolva', '')
    cantidadInp = float(request.POST.get('cantidad', 0))
    restante = 0
    cantidad = 0 
    tolva_save = tblTolva.objects.get(ID=tolva)
    capacidad = tolva_save.Capacidad
    if cantidadInp > capacidad:
        restante = cantidadInp - capacidad 
        cantidad = capacidad
    else:
        cantidad = cantidadInp
    
    ultimo_id = tblFormulado.objects.order_by('-ID').first()
    if ultimo_id:
        ultimo_folio = ultimo_id.ID + 1
    else:
        ultimo_folio = 1
    
    FechaDeHoy = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')
    
    if producto is not None and producto != '':
        FiltradoProducto= tblProductos.objects.get(ID=producto)
        SProducto = tblProductos.objects.all().values('ID', 'Descripcion').exclude(ID=1)
        FiltradoTolva= tblTolva.objects.get(ID=tolva)
        STolva = tblTolva.objects.exclude(ID = 1).values('ID','IDProducto_id__Descripcion', 'Alias', 'IDProducto_id', 'IDEstatus_id', 'Capacidad')
        FiltradoReceta = (
        tblReceta.objects.filter(IDProductos=producto).annotate(cantidad_porcentaje=ExpressionWrapper(Value(cantidad) * (F('Porcentaje') / 100),
                output_field=FloatField()),
            cantidad_restante=ExpressionWrapper(Value(restante) * (F('Porcentaje') / 100),output_field=FloatField())
        ).values( 'ID', 'Folio', 'IDMateriaPrima_id__Descripcion', 'IDMateriaPrima_id', 'Merma', 'Porcentaje', 'cantidad_porcentaje', 'cantidad_restante'))
        
        return render(request, 'FormulacionConsolidacion/index.html',{ 'FiltradoReceta':FiltradoReceta, 'SProducto':SProducto, 'FechaDeHoy':FechaDeHoy,
          'STolva':STolva, 'FiltradoProducto':FiltradoProducto,'FiltradoTolva':FiltradoTolva, 'cantidad':cantidadInp, 'ultimo_folio':ultimo_folio, 'restante':restante, 'ServiciosWeb':ServiciosWeb})
    else:
        FiltradoProducto= tblProductos.objects.filter(ID=1).first()
        FiltradoTolva= tblTolva.objects.filter(ID=2).first()
        STolva = tblTolva.objects.exclude(ID = 1).all()
        cantidad= 0
    
    return render(request, 'FormulacionConsolidacion/index.html',{'FiltradoTolva':FiltradoTolva, 'FechaDeHoy':FechaDeHoy,
    'FiltradoProducto':FiltradoProducto, 'STolva':STolva, 'cantidad':cantidad, 'ultimo_folio':ultimo_folio, 'restante':restante, 'ServiciosWeb':ServiciosWeb})