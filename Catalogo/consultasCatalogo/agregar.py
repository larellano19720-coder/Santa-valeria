from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from datetime import datetime, date
from Aplicacion.views import servicioActivo
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GUARDAR FORMULARIO CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# -------------------------------------------------------OPERADORES--------------------------------------------------------
def guardarOperador(request):
    clave = request.POST['clave']
    nombre = request.POST['nombre'].upper()
    estatus = request.POST['estatus']

    clave_int = int(clave)
    formatoClave = 'F-{:06d}'.format(clave_int)


    existente = tblOperadores.objects.filter(Descripcion=nombre).exists()
    if existente:
        errorCol = 'error'
        FEstatus = tblEstatus.objects.all() 
        messages.error(request, f'El Operador {nombre} ya ha sido registrado antreriormente')
        columnas = {'clave':clave, 'FEstatus': FEstatus, 'errorCol':errorCol}
        return render(request, "Operador/form.html", columnas)
    else:
        tblOperadores.objects.create(
            Clave = formatoClave,  Descripcion=nombre, IDEstatus_id = estatus
        )
        messages.success(request, f'El Operador {nombre} se ha registrado exitosamente')


    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('catalogo:T_Operador')
        elif 'agregar' in request.POST:
            return redirect('catalogo:F_Operador')
    else:
        return redirect('catalogo:T_Operador')   

# -----------------------------------------------------MATERIAS PRIMAS-----------------------------------------------------
def guardarMateriasPrimas(request):
    clave = request.POST['clave']
    descripcion = request.POST['descripcion'].upper()
    precio = request.POST['precio']
    merma = request.POST['merma']
    estatus = request.POST['estatus']
    unidad = request.POST['unidad']

    clave_int = int(clave)
    formatoClave = 'F-{:06d}'.format(clave_int)

    existente = tblMateriaPrima.objects.filter(Descripcion=descripcion).exists()
    if existente:
        errorCol = 'error'
        FEstatus=tblEstatus.objects.all()
        FUnidadMedida=tblUnidades.objects.all()
        messages.error(request, f'La Materia Prima {descripcion} ya ha sido registrado antreriormente')
        columnas = {'clave':clave, 'FEstatus':FEstatus,'FUnidadMedida':FUnidadMedida,'errorCol':errorCol}
        return render(request, "Materia Prima/form.html", columnas)
    else:
        tblMateriaPrima.objects.create(
            Clave = formatoClave, Descripcion = descripcion, IDEstatus_id = estatus, 
            IDUnidadMedida_id = unidad, PrecioUnitario = precio, Merma = merma
        )
        messages.success(request, f'La Materia Prima {descripcion} se ha registrado exitosamente')

    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('catalogo:T_MateriaPrima')
        elif 'agregar' in request.POST:
            return redirect('catalogo:F_MateriaPrima')
    else:
        return redirect('catalogo:T_MateriaPrima')   

# --------------------------------------------------------PRODUCTOS--------------------------------------------------------
def guardarProductos(request):
    clave = request.POST['clave']
    descripcion = request.POST['descripcion'].upper()
    precio = request.POST['precio']
    seSirve = request.POST['seSirve']
    estatus = request.POST['estatus']
    unidad = request.POST['unidad']

    clave_int = int(clave)
    formatoClave = 'F-{:06d}'.format(clave_int)

    existente = tblProductos.objects.filter(Descripcion=descripcion).exists()
    if existente:
        errorCol = 'error'
        FEstatus=tblEstatus.objects.all()
        FUnidadMedida=tblUnidades.objects.all()
        messages.error(request, f'El Producto {descripcion} ya ha sido registrado antreriormente')
        columnas = {'clave':clave, 'errorCol':errorCol, 'FEstatus':FEstatus,'FUnidadMedida':FUnidadMedida}
        return render(request, "Producto/form.html", columnas)
    else:
        tblProductos.objects.create(
            Clave = formatoClave, Descripcion = descripcion, IDEstatus_id = estatus, 
            IDUnidadMedida_id = unidad, PrecioUnitario = precio, SeSirve = seSirve
        )
        messages.success(request, f'El Producto {descripcion} se ha registrado exitosamente')


    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('catalogo:T_Producto')
        elif 'agregar' in request.POST:
            return redirect('catalogo:F_Producto')
    else:
        return redirect('catalogo:T_Producto')

# -------------------------------------------------MOVIMIENTOS DE ANIMALES-------------------------------------------------
def guardarRecetas(request):
    ServiciosWeb = servicioActivo() 
    clave = request.POST['clave']
    clave_int = int(clave)
    formatoClave = 'F-{:06d}'.format(clave_int)
 
    AgRecetas = tblProductos.objects.get(ID=clave)
    ClaveProducto = AgRecetas.Clave
    Estatus = AgRecetas.IDEstatus.ID
    Unidad = AgRecetas.IDUnidadMedida.ID
    FiltradoEstatus = tblEstatus.objects.get(ID=Estatus)
    FiltradoUnidad = tblUnidades.objects.get(ID=Unidad)
    FMateriaPrima = tblMateriaPrima.objects.all().order_by('Descripcion')
    Recetas = tblReceta.objects.filter(Folio=ClaveProducto).values('ID', 'Folio',
    'IDMateriaPrima_id__Descripcion', 'Merma', 'Porcentaje')
    proporcion = request.POST['proporcion']
    merma = request.POST['merma']
    materia = request.POST['materia']

    ultimo_id = tblReceta.objects.order_by('-ID').first()
    if ultimo_id:
        ultimo_folio = ultimo_id.ID + 1
    else:
        ultimo_folio = 1


    print(ClaveProducto)
    tblReceta.objects.create(
        Folio = ClaveProducto, IDMateriaPrima_id = materia, Porcentaje = proporcion, Merma = merma, 
        IDProductos_id = clave
    )
    messages.success(request, f'Se ha agregado exitosamente la receta')


    # Filtra los registros basados en IDProductos y suma la columna 'Porcentaje'
    total_porcentaje = tblReceta.objects.filter(IDProductos=clave_int).aggregate(Sum('Porcentaje'))


    # Verifica si el valor de la suma es None y maneja ese caso
    if total_porcentaje['Porcentaje__sum'] is None:
        total = 0
    else:
        total = total_porcentaje['Porcentaje__sum']

    print(total)
    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('catalogo:T_Producto')
        elif 'agregar' in request.POST:
            return render(request, "Producto/agregar.html", {'formatoClave':formatoClave, 'total':total,'ServiciosWeb':ServiciosWeb,
            'Recetas':Recetas,'AgRecetas': AgRecetas,'FiltradoEstatus':FiltradoEstatus, 'FiltradoUnidad':FiltradoUnidad,
            'FMateriaPrima':FMateriaPrima })
    else:
        return redirect('catalogo:T_Producto')
    
# --------------------------------------------------------CORRALES---------------------------------------------------------
def guardarCorrales(request):
    clave = request.POST['clave']
    descripcion = request.POST['descripcion'].upper()
    estatus = request.POST['estatus']
    fecha = request.POST['fecha']

    clave_int = int(clave)
    formatoClave = 'F-{:06d}'.format(clave_int)

    existente = tblCorrales.objects.filter(Descripcion=descripcion).exists()
    if existente:
        errorCol = 'error'
        FEstatus = tblEstatus.objects.all()
        FechaDeHoy = date.today().strftime('%Y-%m-%d') 
        messages.error(request, f'El Corral {descripcion} ya ha sido registrado antreriormente')
        columnas = {'clave':clave,'FEstatus':FEstatus,'FechaDeHoy':FechaDeHoy,'errorCol':errorCol}
        return render(request, "Corral/form.html", columnas)
    else:
        tblCorrales.objects.create(
            Clave = formatoClave, Descripcion = descripcion,
            IDEstatus_id = estatus, Fecha = fecha
        )
        messages.success(request, f'El Corral {descripcion} se ha registrado exitosamente')

    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('catalogo:T_Corral')
        elif 'agregar' in request.POST:
            return redirect('catalogo:F_Corral')
    else:
        return redirect('catalogo:T_Corral')  

# ------------------------------------------------------TIPO ANIMALES------------------------------------------------------
def guardarTolva(request):
    clave = request.POST['clave']
    alias = request.POST['alias'].upper()
    marca = request.POST['marca'].upper()
    modelo = request.POST['modelo'].upper()
    capacidad = request.POST['capacidad']
    estatus = request.POST['estatus']
    producto = request.POST['producto']
    unidad = request.POST['unidad']
    
    
    clave_int = int(clave)
    formatoClave = 'F-{:06d}'.format(clave_int)
    
    existente = tblTolva.objects.filter(Alias=alias).exists()
    if existente:
        errorCol = 'error'
        FEstatus = tblEstatus.objects.all()
        FUnidadMedida=tblUnidades.objects.all()
        messages.error(request, f'La tolva {alias} ya ha sido registrado antreriormente')
        columnas = {'clave': clave, 'errorCol':errorCol, 'FUnidadMedida':FUnidadMedida}
        return render(request, "Tolva/form.html", columnas)
    else:
        tblTolva.objects.create(
            Clave = formatoClave, Marca=marca, Modelo = modelo,
            Capacidad = capacidad, Alias=alias, IDEstatus_id = estatus, 
            IDProducto_id = producto, UdeM_id = unidad
        )
        messages.success(request, f'La tolva {alias} se ha registrado exitosamente')

    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('catalogo:T_Tolva')
        elif 'agregar' in request.POST:
            return redirect('catalogo:F_Tolva')
    else:
        return redirect('catalogo:T_Tolva')
