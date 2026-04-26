from django.shortcuts import redirect, render
from django.contrib import messages
# LLAMAR ARCHIVOS LOCALES
from django.db.models import Q
from Aplicacion.forms import *
from Aplicacion.models import *
from django.utils import timezone
from Aplicacion.views import servicioActivo
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ACTUALIZAR DATOS CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# -------------------------------------------------------OPERADORES--------------------------------------------------------
def actualizarOperador(request):
    id = request.POST['id']
    clave = request.POST['clave']
    descripcion = request.POST['operador'].upper().strip()
    estatus = request.POST['estatus']

    operador_existente = tblOperadores.objects.filter(Descripcion=descripcion).exclude(ID=id).exists()
    if operador_existente:
        messages.error(request, f'El Operador "{descripcion}" ya ha sido registrado anteriormente.')
        IDNumber = int(id)
        return redirect('catalogo:E_Operador', IDNumber)
    else:
        operador = tblOperadores.objects.get(ID=id)
        Estatus_instancia = tblEstatus.objects.get(ID=estatus)

        operador.Descripcion = descripcion
        operador.IDEstatus = Estatus_instancia
        operador.save()

        messages.success(request, f'El Operador "{descripcion}" se ha actualizado exitosamente.')
    return redirect('catalogo:T_Operador')

# -----------------------------------------------------MATERIAS PRIMAS-----------------------------------------------------
def actualizarMateriaPrima(request):
    id = request.POST['id']
    clave = request.POST['clave']
    materia_v = request.POST['materia'].upper().strip()
    precio_v = request.POST['precio']
    merma_v = request.POST['merma']
    estatus_v = request.POST['estatus']
    unidad_v = request.POST['unidad']

    materia_existente = tblMateriaPrima.objects.filter(Descripcion=materia_v).exclude(ID=id).exists()
    if materia_existente:
        messages.error(request, f'La Materia Prima "{materia_v}" ya ha sido registrado anteriormente.')
        IDNumber = int(id)
        return redirect('catalogo:E_MateriaPrima', IDNumber)
    else:
        mateira_prima = tblMateriaPrima.objects.get(ID=id)
        Estatus_instancia = tblEstatus.objects.get(ID=estatus_v)
        Unidad_instancia = tblUnidades.objects.get(ID=unidad_v)

        mateira_prima.Descripcion = materia_v
        mateira_prima.PrecioUnitario = precio_v
        mateira_prima.Merma = merma_v
        mateira_prima.IDEstatus = Estatus_instancia
        mateira_prima.IDUnidadMedida = Unidad_instancia
        mateira_prima.save()
        messages.success(request, f'La Materia Prima "{materia_v}" se ha actualizado exitosamente.')
    
    return redirect('catalogo:T_MateriaPrima')

# --------------------------------------------------------PRODUCTOS--------------------------------------------------------
def actualizarProductos(request):
    id = request.POST['id']
    clave = request.POST['clave']
    producto_v = request.POST['producto'].upper().strip()
    precio_v = request.POST['precio']
    estatus_v = request.POST['estatus']
    unidad_v = request.POST['unidad']
    seSirve_v = request.POST['seSirve']

    producto_existente = tblProductos.objects.filter(Descripcion=producto_v).exclude(ID=id).exists()
    if producto_existente:
        messages.error(request, f'El Producto "{producto_v}" ya ha sido registrado anteriormente.')
        IDNumber = int(id)
        return redirect('catalogo:E_Producto', IDNumber)
    else:
        producto_save = tblProductos.objects.get(ID=id)
        Estatus_instancia = tblEstatus.objects.get(ID=estatus_v)
        Unidad_instancia = tblUnidades.objects.get(ID=unidad_v)

        producto_save.Descripcion = producto_v
        producto_save.PrecioUnitario = precio_v
        producto_save.SeSirve = seSirve_v
        producto_save.IDEstatus = Estatus_instancia
        producto_save.IDUnidadMedida = Unidad_instancia
        producto_save.save()

        messages.success(request, f'El Producto "{producto_v}" se ha actualizado exitosamente.')
    
 
    return redirect('catalogo:T_Producto')

# -------------------------------------------RECETAS DE PRODUCTOS----------------------------------------------------
def actualizarRecetasProductos(request):
    id = request.POST['id']
    folio_v = request.POST['folio']
    materia_v = request.POST['materia']
    proporcion_v = request.POST['proporcion']
    merma_v = request.POST['merma']
    producto_v = request.POST['producto']
    
    recetas = tblReceta.objects.get(ID=id)
    materia_instancia = tblMateriaPrima.objects.get(ID=materia_v)
   
    recetas.IDMateriaPrima = materia_instancia
    recetas.Porcentaje = proporcion_v
    recetas.Merma = merma_v
    recetas.save()

    messages.success(request, f'La receta "{folio_v}" se ha actualizado exitosamente.')


    return redirect('catalogo:AR_Producto', ID=producto_v)
# --------------------------------------------------------CORRALES---------------------------------------------------------
def actualizarCorral(request):
    ServiciosWeb = servicioActivo() 
    id = request.POST['id']
    clave = request.POST['clave']
    corral_v = request.POST['corral'].upper().strip()
    capacidad_v = 0
    estatus_v = request.POST['estatus']
    fecha_v = request.POST['fecha']
    
    corral_existente = tblCorrales.objects.filter(Descripcion=corral_v).exclude(ID=id).exists()
    if corral_existente:
        messages.error(request, f'El Corral "{corral_v}" ya ha sido registrado anteriormente.')
        IDNumber = int(id)
        return redirect('catalogo:E_Corral', IDNumber)
    else:
        corral_save = tblCorrales.objects.get(ID=id)
        Estatus_instancia = tblEstatus.objects.get(ID=estatus_v)

        corral_save.Clave = clave
        corral_save.Descripcion = corral_v
        corral_save.Fecha = fecha_v
        corral_save.IDEstatus = Estatus_instancia
        corral_save.save()

        messages.success(request, f'El Corral "{corral_v}" se ha actualizado exitosamente.')
    return redirect('catalogo:T_Corral')

# ------------------------------------------------------TIPO ANIMALES------------------------------------------------------
def actualizarTolva(request):
    id = request.POST['id']
    clave = request.POST['clave']
    alias = request.POST['alias'].upper()
    marca = request.POST['marca'].upper()
    modelo = request.POST['modelo'].upper()
    capacidad = request.POST['capacidad']
    estatus = request.POST['estatus']
    unidad = request.POST['unidad']
    
    tolva_existente = tblTolva.objects.filter(Alias=alias).exclude(ID=id).exists()
    if tolva_existente:
        messages.error(request, f'La tolva "{alias}" ya ha sido registrado anteriormente.')
        IDNumber = int(id)
        return redirect('catalogo:E_Tolva', IDNumber)
    else:
        tolva_save = tblTolva.objects.get(ID=id)
        Estatus_instancia = tblEstatus.objects.get(ID=estatus)
        Unidades_instancia = tblUnidades.objects.get(ID=unidad)

        tolva_save.Alias = alias
        tolva_save.Marca = marca
        tolva_save.Modelo = modelo
        tolva_save.Capacidad = capacidad
        tolva_save.IDEstatus = Estatus_instancia
        tolva_save.UdeM = Unidades_instancia
        
        tolva_save.save()
        messages.success(request, f'La tolva "{alias}" se ha actualizado exitosamente.')
    return redirect('catalogo:T_Tolva')