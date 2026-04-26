from django.shortcuts import redirect,render
from django.contrib import messages
from django.db.models import Sum
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from datetime import datetime, date
from django.utils import timezone
from django.db.models import Q
from Aplicacion.views import servicioActivo
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GUARDAR FORMULARIO PROCESOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def guardarSolicitudServido(request):
    if request.method == 'POST':
        # VARIABLES PARA CONFIGURACION
        porcentaje_v = int(request.POST.get('porcentaje'))
        # LLENAR LA TABLA DE TBLREPARTIDOR
        id_v = request.POST.getlist('id[]')
        folio_v = int(request.POST.get('folio'))
        cantidadSol_v = request.POST.getlist('cantidadSol[]')
        cantidadAnimales_v = request.POST.getlist('cantidadAnimales[]')
        producto_v = request.POST.getlist('producto[]')
        seSirve_v = request.POST.getlist('seSirve[]')

        FechaDeHoy = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')
        
        solicitudes = []
        for i in range(len(cantidadSol_v)):
            if cantidadSol_v[i]  and int(cantidadSol_v[i]) != 0:
                solicitud = {
                    'id': id_v[i],
                    'producto': producto_v[i],
                    'seSirve': seSirve_v[i],
                    'cantidadSol': int(cantidadSol_v[i]),
                    'cantidadAnimales': int(cantidadAnimales_v[i])
                }
                solicitudes.append(solicitud)

        for solicitud in solicitudes:
            folio_v += 1
            clave_int = folio_v
            formatoClave = 'S-{:06d}'.format(clave_int)         
            tblRepartidor.objects.create(Folio = formatoClave, IDCorral_id =solicitud['id'], IDProducto_id = solicitud['producto'], IDTolva_id = 2,
            IDEstatus_id = 3, CantidadSolicitada = solicitud['cantidadSol'], Cantidad1 = 0,Cantidad2 = 0, 
            FechaSol = FechaDeHoy, Porcentaje = porcentaje_v, SeSirve = solicitud['seSirve'], CantidadAnimales =  solicitud['cantidadAnimales'])             

        porcentaje_save = tblConfiguracion.objects.get(ID=1)
        porcentaje_save.Porcentaje = porcentaje_v
        porcentaje_save.save()

        messages.success(request, f'El Servido se ha actualizado exitosamente.')
        print("Sevidopr")
        return redirect('proceso:T_Solicitud_Servidos')


# -------------------------------------------------SERVIDOS MANUALES-------------------------------------------------
def guardarServidosManuales(request):
    ServiciosWeb = servicioActivo() 
    clave = request.POST['folio']
    cliente = request.POST['cliente']
    corral = request.POST['corral']
    producto = request.POST['producto']
    estatus = request.POST['estatus']
    prioridad = request.POST['prioridad']
    cantidadSol = request.POST['cantidadSol']
    cantidadSer = request.POST['cantidadSer']
    fechaSol = request.POST['fechaSol']
    fechaSer = request.POST['fechaSer']

    clave_int = int(clave)
    formatoClave = 'F-{:06d}'.format(clave_int)


    tblRepartidor.objects.create(Folio = formatoClave,  IDCliente_id = cliente, IDCorral_id =corral, IDProducto_id = producto, 
    IDEstatus_id = estatus, CantidadSolicitada = cantidadSol, CantidadServida =cantidadSer, 
    Prioridad =prioridad, FechaSol = fechaSol, FechaServida = fechaSer
    ) 

    messages.success(request, 'El Servido Manual se ha registrado exitosamente')
    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('T-Servidos')
        elif 'agregar' in request.POST:
            return redirect('F-Servidos')
    else:
        return redirect('T-Servidos')


    clave = request.POST['clave']

    producto = request.POST['producto']
  
    clave_int = int(clave)
    formatoClave = 'F-{:06d}'.format(clave_int)

    # tecnicos
    Tecnico_v = request.POST['tecnico'].upper()
    NombreTabla_v = 'Inventario Productos'
    IDFilaTabla_v = formatoClave
    AreaRegistro_v = 'Procesos'
    IDFila_v = clave

    messages.success(request, 'El Inventario de productos se ha registrado exitosamente')
    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('T-InventarioProductos')
        elif 'agregar' in request.POST:
            return redirect('F-InventarioProductos')
    else:
        return redirect('T-InventarioProductos')