from django.shortcuts import render
from django.db.models import Q
from django.db.models import Sum
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from Aplicacion.views import servicioActivo
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< EDITAR FORMULARIO CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# -------------------------------------------------------OPERADORES--------------------------------------------------------
def editarOperador(request, ID):
    ServiciosWeb = servicioActivo() 
    TEOperador = tblOperadores.objects.get(ID=ID)
    Estatus = TEOperador.IDEstatus.ID
    FiltradoEstatus= tblEstatus.objects.get(ID=Estatus)
    FEEstatus = tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    return render(request, "Operador/edit.html",{'TEOperador': TEOperador,'FiltradoEstatus': FiltradoEstatus,'FEEstatus': FEEstatus, 'ServiciosWeb':ServiciosWeb})

# -----------------------------------------------------MATERIAS PRIMAS-----------------------------------------------------
def editarMateriaPrima(request, ID):
    ServiciosWeb = servicioActivo() 
    TEMateriaPrima = tblMateriaPrima.objects.get(ID=ID)
    Estatus = TEMateriaPrima.IDEstatus.ID
    Unidad = TEMateriaPrima.IDUnidadMedida.ID
    FiltradoEstatus= tblEstatus.objects.get(ID=Estatus)
    FiltradoUnidad= tblUnidades.objects.get(ID=Unidad)
    FEEstatus = tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    FEUnidad = tblUnidades.objects.all().order_by('Descripcion')
    return render(request, "MateriaPrima/edit.html",{'TEMateriaPrima': TEMateriaPrima,'FiltradoEstatus': FiltradoEstatus,'FiltradoUnidad': FiltradoUnidad,'FEEstatus': FEEstatus,'FEUnidad': FEUnidad, 'ServiciosWeb':ServiciosWeb})

# --------------------------------------------------------PRODUCTOS--------------------------------------------------------
def editarProducto(request, ID):
    ServiciosWeb = servicioActivo() 
    TEProductos = tblProductos.objects.get(ID=ID)
    Estatus = TEProductos.IDEstatus.ID
    Unidad = TEProductos.IDUnidadMedida.ID
    FiltradoEstatus= tblEstatus.objects.get(ID=Estatus)
    FiltradoUnidad= tblUnidades.objects.get(ID=Unidad)
    FEEstatus = tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    FEUnidad = tblUnidades.objects.all().order_by('Descripcion')
    return render(request, "Producto/edit.html",{'TEProductos': TEProductos,'FiltradoEstatus': FiltradoEstatus,'FiltradoUnidad': FiltradoUnidad,'FEEstatus': FEEstatus,'FEUnidad': FEUnidad, 'ServiciosWeb':ServiciosWeb})

def editarProductoReceta(request, ID):
    ServiciosWeb = servicioActivo() 
    TRecetas= tblReceta.objects.get(ID=ID)
    proporcion = TRecetas.Porcentaje
    folio = TRecetas.IDProductos
    animal = TRecetas.IDMateriaPrima.ID
    FiltradoMateriaPrima = tblMateriaPrima.objects.get(ID=animal)
    FEMateriaPrima = tblMateriaPrima.objects.all()
    # Filtra los registros basados en IDProductos y suma la columna 'Porcentaje'
    total_porcentaje = tblReceta.objects.filter(IDProductos=folio).aggregate(Sum('Porcentaje'))

    # Verifica si el valor de la suma es None y maneja ese caso
    if total_porcentaje['Porcentaje__sum'] is None:
        total = 0
    else:
        total = total_porcentaje['Porcentaje__sum']  - proporcion
    print(total)
    return render(request, "Producto/editReceta.html",{ 'total':total, 
    'TRecetas': TRecetas, 'FiltradoMateriaPrima': FiltradoMateriaPrima, 'FEMateriaPrima': FEMateriaPrima, 'ServiciosWeb':ServiciosWeb })

# --------------------------------------------------------CORRALES---------------------------------------------------------
def editarCorral(request, ID):
    ServiciosWeb = servicioActivo() 
    TECorrales= tblCorrales.objects.get(ID=ID)
    Estatus = TECorrales.IDEstatus.ID
    fecha = TECorrales.Fecha
    FiltradoEstatus= tblEstatus.objects.get(ID=Estatus)
    FEEstatus = tblEstatus.objects.filter(ID__lte=2).order_by('Descripcion')
    return render(request, "Corral/edit.html",{'fecha':fecha, 'TECorrales': TECorrales,'FiltradoEstatus': FiltradoEstatus,'FEEstatus': FEEstatus, 'ServiciosWeb':ServiciosWeb})

# ------------------------------------------------------TOLVA------------------------------------------------------
def editarTolva(request, ID):
    ServiciosWeb = servicioActivo() 
    TETolva = tblTolva.objects.get(ID=ID)
    Estatus = TETolva.IDEstatus.ID
    Unidad = TETolva.UdeM.ID
    FiltradoEstatus= tblEstatus.objects.get(ID=Estatus)
    FiltradoUnidad= tblUnidades.objects.get(ID=Unidad)
    FEEstatus = tblEstatus.objects.filter(ID__gte=4, ID__lte=6)
    FEUnidades = tblUnidades.objects.all()
    return render(request, "Tolva/edit.html",{ 'FEUnidades':FEUnidades, 
        'TETolva': TETolva,'FiltradoEstatus': FiltradoEstatus,'FEEstatus': FEEstatus, 'FiltradoUnidad':FiltradoUnidad, 'ServiciosWeb':ServiciosWeb})
