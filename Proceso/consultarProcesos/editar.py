from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from datetime import datetime, timedelta
from django.db.models import F, Value
from django.db.models.functions import Coalesce
from Aplicacion.views import servicioActivo
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< EDITAR FORMULARIO PROCESOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------SERVIDOS--------------------------------------------------------
# --------------------------------------------------------CORRALES---------------------------------------------------------
def editarSolicitudServidos(request):
    ServiciosWeb = servicioActivo() 
    if request.method == 'POST':
        fecha_str = request.POST.get('fecha')
        porcentaje = request.POST.get('porcentaje')
        estatus = request.POST.get('estatus')

        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")

        TEServidos = tblRepartidor.objects.filter(
            FechaSol__gte=fecha,
            FechaSol__lt=fecha + timedelta(minutes=2)
        ).values(
            'ID',
            'Folio',
            'IDCorral_id',
            'IDCorral_id__Descripcion',
            'IDProducto_id__Descripcion',
            'IDEstatus_id__Descripcion',
            'IDProducto_id',
            'IDEstatus_id',
            'CantidadAnimales',
            'CantidadSolicitada',
            'SeSirve',
            'FechaSol',
            'FechaServida1'
        )

        # 2️⃣ IDs de corrales ya usados
        corrales_usados = tblRepartidor.objects.filter(
            FechaSol__gte=fecha,
            FechaSol__lt=fecha + timedelta(minutes=2)
        ).values_list('IDCorral_id', flat=True).distinct()

        # 3️⃣ Corrales que NO están en repartidor
        corrales_faltantes = tblCorrales.objects.exclude(
            ID__in=corrales_usados
        ).values(
            IDCorral_id=F('ID'),

            IDCorral_id__Descripcion=F('Descripcion'),

        )        
        FECorral = tblCorrales.objects.all().order_by('Descripcion')
        FEProducto = tblProductos.objects.all().exclude(ID = 1).order_by('Descripcion')
        FEEstatus = tblEstatus.objects.filter(ID=3).order_by('Descripcion')
        
    return render(request, "SolicitudServido/edit.html",{'TEServidos': TEServidos, 'corrales_faltantes':corrales_faltantes,  'fecha':fecha, 'porcentaje':porcentaje,
    'FECorral': FECorral,'FEProducto': FEProducto, 'FEEstatus': FEEstatus, 'ServiciosWeb':ServiciosWeb, 'estatus':estatus})


def agregarSolicitudServidos(request):
    ServiciosWeb = servicioActivo() 
    if request.method == 'POST':
        fecha_str = request.POST.get('fecha')
        porcentaje = request.POST.get('porcentaje')
        estatus = request.POST.get('estatus')

        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")

        TEServidos = tblRepartidor.objects.filter(
            FechaSol__gte=fecha,
            FechaSol__lt=fecha + timedelta(minutes=2)
        ).values(
            'ID',
            'Folio',
            'IDCorral_id',
            'IDCorral_id__Descripcion',
            'IDProducto_id__Descripcion',
            'IDEstatus_id',
            'IDEstatus_id__Descripcion',
            'IDProducto_id',
            'IDEstatus_id',
            'CantidadSolicitada',
            'CantidadAnimales',
            'SeSirve',
            'FechaSol',
            'FechaServida1'
        )

        # 2️⃣ IDs de corrales ya usados
        corrales_usados = tblRepartidor.objects.filter(
            FechaSol__gte=fecha,
            FechaSol__lt=fecha + timedelta(minutes=2)
        ).values_list('IDCorral_id', flat=True).distinct()

        # 3️⃣ Corrales que NO están en repartidor
        corrales_faltantes = tblCorrales.objects.exclude(
            ID__in=corrales_usados
        ).values(
            IDCorral_id=F('ID'),

            IDCorral_id__Descripcion=F('Descripcion'),

        )

        # 4️⃣ Unir todo
        todos_corrales = list(TEServidos) + list(corrales_faltantes)

        FECorral = tblCorrales.objects.all().order_by('Descripcion')
        FEProducto = tblProductos.objects.all().exclude(ID = 1).order_by('Descripcion')
        FEEstatus = tblEstatus.objects.filter(ID=3).order_by('Descripcion')
    return render(request, "SolicitudServido/edit.html",{'TEServidos': todos_corrales, 'fecha':fecha, 'porcentaje':porcentaje,
    'FECorral': FECorral,'FEProducto': FEProducto, 'FEEstatus': FEEstatus, 'ServiciosWeb':ServiciosWeb, 'estatus':estatus})


def editarServidosManuales(request, ID):
    ServiciosWeb = servicioActivo() 
    TEServidos= tblRepartidor.objects.get(ID=ID)
    Estatus = TEServidos.IDEstatus.ID
    Producto = TEServidos.IDProducto.ID
    Corral = TEServidos.IDCorral.ID
    fecha = TEServidos.FechaSol
    fechaServida = TEServidos.FechaServida1
    FiltradoEstatus= tblEstatus.objects.get(ID=Estatus)
    FiltradoProducto= tblProductos.objects.get(ID=Producto)
    FiltradoCorral= tblCorrales.objects.get(ID=Corral)
    FECorral = tblCorrales.objects.all().order_by('Descripcion')
    FEProducto = tblProductos.objects.all().order_by('Descripcion')
    FEEstatus = tblEstatus.objects.filter(ID=3).order_by('Descripcion')
    return render(request, "Servido Manual/edit.html",{'TEServidos': TEServidos, 'fecha':fecha,
    'FiltradoEstatus': FiltradoEstatus,'FiltradoProducto': FiltradoProducto,
    'FiltradoCorral': FiltradoCorral,'FECorral': FECorral,'FEProducto': FEProducto, 'fechaServida':fechaServida,
    'FEEstatus': FEEstatus, 'ServiciosWeb':ServiciosWeb})

