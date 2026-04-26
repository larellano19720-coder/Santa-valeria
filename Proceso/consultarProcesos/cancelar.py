from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from Aplicacion.forms import *
from Aplicacion.models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta

def cancelarServidos(request):
    if request.method == 'POST':
        id_v = request.POST.get('id')

        objeto = get_object_or_404(tblRepartidor, ID=id_v)
        objeto.delete()

        return JsonResponse({
            'status': 'ok',
            # opcional si quieres redirigir
            # 'redirect_url': reverse('proceso:editarSolicitudServidos')
        })

def cancelarOrdenServidos(request):

    if request.method == "POST":

        fecha_str = request.POST.get('fecha')
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")

        # regresar los visibles a estatus 3
        tblRepartidor.objects.filter(
            FechaSol__gte=fecha,
            FechaSol__lt=fecha + timedelta(minutes=2)
        
        ).update(IDEstatus_id=3)

        print("Registro")
        return JsonResponse({
            "ok": True,
            'redirect_url': reverse('proceso:T_Solicitud_Servidos')
        })
        
def eliminarOrdenServidos(request):


    if request.method == "POST":

        fecha_str = request.POST.get('fecha')
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")

        # regresar los visibles a estatus 3
        tblRepartidor.objects.filter(
            FechaSol__gte=fecha,
            FechaSol__lt=fecha + timedelta(minutes=2)
        
        ).delete()

        print("Registro")
        return JsonResponse({
            "ok": True,
            'redirect_url': reverse('proceso:T_Solicitud_Servidos')
        })