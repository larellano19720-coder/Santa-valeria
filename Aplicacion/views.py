from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import  Sum, Q
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

# LLAMAR ARCHIVOS LOCALES
from .forms import *
from .models import *



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def servicioActivo():
    ServiciosWeb = tblServiciosWeb.objects.get(ID=1)
    FechaDeHoy = date.today().strftime('%Y-%m-%d')
    FechaDeHoy = date.today()

    if ServiciosWeb.FechaVencimiento <= FechaDeHoy:
        fecha_vencimiento = datetime.combine(
            ServiciosWeb.FechaVencimiento, datetime.min.time())
        diferencia = FechaDeHoy - fecha_vencimiento.date()
        dias_pasados = diferencia.days
        print(dias_pasados)

        EstadoDePago = False
        save_servicio = tblServiciosWeb.objects.get(ID=1)
        save_servicio.EstadoPago = EstadoDePago
        save_servicio.save()

        if ServiciosWeb.EstadoPago == False and dias_pasados >= 5:
            Servicios = False
            save_servicio = tblServiciosWeb.objects.get(ID=1)
            save_servicio.Servicio = Servicios
            save_servicio.save()
    return ServiciosWeb

def estadoPago(request):
    TServicio = tblServiciosWeb.objects.all()
    ServiciosWeb = tblServiciosWeb.objects.get(ID=1)
    FechaDeHoy = date.today().strftime('%Y-%m-%d')
    FechaDeHoy = date.today()

    if ServiciosWeb.FechaVencimiento <= FechaDeHoy:
        fecha_vencimiento = datetime.combine(
            ServiciosWeb.FechaVencimiento, datetime.min.time())
        diferencia = FechaDeHoy - fecha_vencimiento.date()
        dias_pasados = diferencia.days
        EstadoDePago = False
        save_servicio = tblServiciosWeb.objects.get(ID=1)
        save_servicio.EstadoPago = EstadoDePago
        save_servicio.save()
        dias_restantes = 5-dias_pasados


        if ServiciosWeb.EstadoPago == False and dias_pasados >= 5:
            Servicios = False
            save_servicio = tblServiciosWeb.objects.get(ID=1)
            save_servicio.Servicio = Servicios
            save_servicio.save()
    else:
        fecha_vencimiento = datetime.combine(
            ServiciosWeb.FechaVencimiento, datetime.min.time())
        diferenciaVencer = fecha_vencimiento.date() - FechaDeHoy
        dias_faltantes = diferenciaVencer.days
        dias_restantes = dias_faltantes
    return render(request, 'Configuracion/pagos/index.html', {'ServiciosWeb': ServiciosWeb, 'dias_restantes': dias_restantes, 'TServicio': TServicio})


def registrarPago(request):
    id = 1
    save_pago = tblServiciosWeb.objects.get(ID=id)
    fechaVencimiento = save_pago.FechaVencimiento

    if 'aplazar' in request.POST:
        ServicioActivo = True
        PagoActivo = True
        fechaFinal = fechaVencimiento + relativedelta(months=1)
        messages.success(request, f'El pago se ha autorizado correctamente')
    elif 'cancelar'in request.POST:
        ServicioActivo = False
        PagoActivo = False
        fechaFinal = date.today().strftime('%Y-%m-%d')
        messages.error(request, f'El servicio se ha cancelado')

    # Obtener la fecha de vencimiento actual y agregar 30 días
    fechaActualizada = fechaFinal
    save_pago.Servicio = ServicioActivo 
    save_pago.EstadoPago = PagoActivo
    save_pago.FechaVencimiento = fechaActualizada
    save_pago.save()

    return redirect('Pagos')    
    
def NoPago(request):
    ServiciosWeb = servicioActivo()
    return render(request, 'Servicio/Sin Servicio/index.html',{'ServiciosWeb': ServiciosWeb})    
    

def menuInfo(request):
    ServiciosWeb = servicioActivo()    
    ContOperadores = tblOperadores.objects.count()
    ContMateriaPrima = tblMateriaPrima.objects.count()
    ContProductos = tblProductos.objects.count()
    ContCorrales = tblCorrales.objects.count()
    ContTolva = tblTolva.objects.count()


    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Tolvas cargadas >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    tolvas = tblTolva.objects.values('ID', 'Capacidad', 'Alias').exclude(ID = 1)
    servido_por_tolva = (tblRepartidor.objects.filter(IDEstatus_id=8).values('IDTolva').annotate(total=Sum('CantidadSolicitada')).exclude(IDTolva = 1))
    servido_dict = {item['IDTolva']: item['total'] for item in servido_por_tolva}
    datos_tolvas = []
    for tolva in tolvas:
        id_tolva = tolva['ID']
        capacidad = tolva['Capacidad']
        alias = tolva['Alias']
        cantidad = servido_dict.get(id_tolva, 0)
        porcentaje = round((cantidad / capacidad) * 100, 2) if capacidad > 0 else 0
        datos_tolvas.append({
            'alias': alias,
            'capacidad': capacidad,
            'cantidad': cantidad,
            'porcentaje': porcentaje
        })


   
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Conteo de servidos >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    PServidosRegistros = tblRepartidor.objects.all()
    registros = PServidosRegistros.count()
    
    PServidosPendientes = tblRepartidor.objects.filter(Q(IDEstatus_id = 3) | Q(IDEstatus_id=9)).all()
    pendientes = PServidosPendientes.count()

    PServidosManual = tblRepartidor.objects.filter(IDEstatus_id = 7).all()
    manuales = PServidosManual.count()

    PServidosConsolidacion = tblRepartidor.objects.filter(IDEstatus_id= 8).all()
    tolva = PServidosConsolidacion.count()
    
    PServidosConsolidacion = tblRepartidor.objects.filter(Q(IDEstatus_id =  10) | Q(IDEstatus_id = 11)).all()
    servidos = PServidosConsolidacion.count()    
    

    return render(request, 'Menu/index.html', {'ContOperadores': ContOperadores, 'pendientes':pendientes, 'servidos':servidos, 'tolva':tolva,
    'ContMateriaPrima': ContMateriaPrima, 'ContProductos': ContProductos, 'ContCorrales': ContCorrales, 'ContTolva': ContTolva, 
    'datos_tolvas':datos_tolvas, 'ServiciosWeb': ServiciosWeb, 'manuales':manuales, 'registros':registros
    })
    
    
    
    
    
    
    
    
    
    
    
    
    
    
