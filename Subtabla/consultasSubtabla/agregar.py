from django.shortcuts import render, redirect
from django.contrib import messages

# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from datetime import datetime, date
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GUARDAR FORMULARIO SubTablas >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------
def guardarEstatus(request):
    clave = request.POST['clave']
    Descripcion_v = request.POST['descripcion'].upper()

    clave_int = int(clave)
    formatoClave = 'F-{:06d}'.format(clave_int)
    
    existente = tblEstatus.objects.filter(Descripcion=Descripcion_v).exists()
    if existente:
        errorCol = 'error'
        messages.error(request, f'El esatus "{Descripcion_v}" ya ha sido registrado antreriormente')
        columnas = {'clave': clave, 'errorCol':errorCol}
        return render(request, "Estatus/form.html", columnas)
    else:
        tblEstatus.objects.create(
            Clave = formatoClave, Descripcion=Descripcion_v
        )
        messages.success(request, f'El estatus "{Descripcion_v}" se ha registrado exitosamente')

    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('subtabla:T_Estatus')
        elif 'agregar' in request.POST:
            return redirect('subtabla:F_Estatus')
    else:
        return redirect('subtabla:T_Estatus')


def guardarUnidadMedida(request):
    clave = request.POST['clave']
    Descripcion_v = request.POST['descripcion'].upper()
    Abreviacion_v = request.POST['abreviacion']
    
    clave_int = int(clave)
    formatoClave = 'F-{:06d}'.format(clave_int)

    existente = tblUnidades.objects.filter(Descripcion=Descripcion_v).exists()
    if existente:
        errorCol = 'error'
        messages.error(request, f'La unidad medida "{Descripcion_v}" ya ha sido registrado antreriormente')
        columnas = {'clave': clave, 'errorCol':errorCol}
        return render(request, "UnidadMedida/form.html", columnas)
    else:
        tblUnidades.objects.create(
            Clave = formatoClave, Descripcion = Descripcion_v, Abreviacion = Abreviacion_v
        )
        messages.success(request, f'La unidad medida "{Descripcion_v}" se ha registrado exitosamente')

    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('subtabla:T_Unidad_Medida')
        elif 'agregar' in request.POST:
            return redirect('subtabla:F_Unidad_Medida')
    else:
        return redirect('subtabla:T_Unidad_Medida')