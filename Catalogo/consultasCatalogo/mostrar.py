from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from django.contrib import messages
from Aplicacion.views import servicioActivo
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

   
# -------------------------------------------------------OPERADORES--------------------------------------------------------
def TablaOperadores(request):
    ServiciosWeb = servicioActivo()     
    TOperadores = tblOperadores.objects.values('ID', 'Clave', 'Descripcion', 'IDEstatus_id__Descripcion')
    return render(request, 'Operador/index.html',{'TOperadores': TOperadores, 'ServiciosWeb':ServiciosWeb})

# -----------------------------------------------------MATERIAS PRIMAS-----------------------------------------------------
def TablaMateriasPrimas(request):
    ServiciosWeb = servicioActivo()     
    TMateriasPrimas = tblMateriaPrima.objects.values('ID', 'Clave', 'Descripcion', 'IDEstatus_id__Descripcion',
                                                     'IDUnidadMedida_id__Abreviacion','PrecioUnitario','Merma')
    return render(request, 'MateriaPrima/index.html',{'TMateriasPrimas': TMateriasPrimas, 'ServiciosWeb':ServiciosWeb})

# --------------------------------------------------------PRODUCTOS--------------------------------------------------------
def AgregarRecetas(request, ID):
    ServiciosWeb = servicioActivo()     
    AgRecetas = tblProductos.objects.get(ID=ID)
    folio = AgRecetas.ID
    folioID = AgRecetas.Clave
    Estatus = AgRecetas.IDEstatus.ID
    Unidad = AgRecetas.IDUnidadMedida.ID
    FiltradoEstatus = tblEstatus.objects.get(ID=Estatus)
    FiltradoUnidad = tblUnidades.objects.get(ID=Unidad)
    FMateriaPrima = tblMateriaPrima.objects.all().order_by('Descripcion')
    Recetas = tblReceta.objects.filter(IDProductos=folio).values('ID', 'IDMateriaPrima_id__Descripcion', 
    'Folio', 'Porcentaje','Merma')

    # Filtra los registros basados en IDProductos y suma la columna 'Porcentaje'
    total_porcentaje = tblReceta.objects.filter(IDProductos=folio).aggregate(Sum('Porcentaje'))


    # Verifica si el valor de la suma es None y maneja ese caso
    if total_porcentaje['Porcentaje__sum'] is None:
        total = 0
    else:
        total = total_porcentaje['Porcentaje__sum']

    print(total)
    
    return render(request, "Producto/agregar.html",{'AgRecetas': AgRecetas, 
    'FiltradoEstatus':FiltradoEstatus, 'FiltradoUnidad':FiltradoUnidad, 'folioID':folioID,
    'FMateriaPrima':FMateriaPrima, 'Recetas':Recetas, 'total':total, 'ServiciosWeb':ServiciosWeb})

def detalleRecetas(request, ID):
    ServiciosWeb = servicioActivo()     
    AgMovimientos = tblProductos.objects.get(ID=ID)
    folio = AgMovimientos.Clave
    Recetas = tblReceta.objects.filter(Folio=folio).values('ID', 'Folio',
    'IDMateriaPrima_id__Descripcion', 'Merma', 'Porcentaje')
    return render(request, 'Producto/verDetalle.html',{'Recetas': Recetas, 'ServiciosWeb':ServiciosWeb})

def TablaProductos(request):
    ServiciosWeb = servicioActivo()     
    TProductos = tblProductos.objects.values('ID', 'Clave', 'Descripcion', 'IDEstatus_id__Descripcion',
                                            'IDUnidadMedida_id__Abreviacion','PrecioUnitario','SeSirve').exclude(ID=1)
    return render(request, 'Producto/index.html',{'TProductos': TProductos, 'ServiciosWeb':ServiciosWeb})

# --------------------------------------------------------CORRALES---------------------------------------------------------
def TablaCorrales(request):
    ServiciosWeb = servicioActivo()     
    TCorrales = tblCorrales.objects.values('ID', 'Clave', 'Descripcion', 'IDEstatus_id__Descripcion','Fecha')
    return render(request, 'Corral/index.html',{'TCorrales': TCorrales, 'ServiciosWeb':ServiciosWeb})

def TablaTolva(request):
    ServiciosWeb = servicioActivo()     
    TTolva = tblTolva.objects.exclude(ID = 1).values('ID', 'Clave', 'Marca', 'Modelo', 'UdeM_id__Abreviacion', 
            'Capacidad', 'IDEstatus_id__Descripcion', 'Alias')
    return render(request, 'Tolva/index.html',{
    'TTolva': TTolva, 'ServiciosWeb':ServiciosWeb})
