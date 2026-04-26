from django.shortcuts import redirect
from django.contrib import messages
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ACTUALIZAR DATOS CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --------------------------------------------------------CLIENTES---------------------------------------------------------
def actualizarEstatus(request):
    id = request.POST['id']
    clave = request.POST['clave']
    descripcion = request.POST['descripcion'].upper().strip()


    nombre_existente = tblEstatus.objects.filter(Descripcion=descripcion).exclude(ID=id).exists()
    if nombre_existente:
        messages.error(request, f'El Estatus "{descripcion}" ya ha sido registrado anteriormente.')
        IDNumber = int(id)
        return redirect('subtabla:E_Estatus', IDNumber)
    else:
        estatus = tblEstatus.objects.get(ID=id)
        estatus.Descripcion = descripcion
        estatus.save()

        messages.success(request, f'El Estatus "{descripcion}" se ha actualizado exitosamente.')

    return redirect('subtabla:T_Estatus')

def actualizarUnidadMedida(request):
    id = request.POST['id']
    clave = request.POST['clave']
    descripcion = request.POST['descripcion'].upper().strip()
    abreviacion = request.POST['abreviacion']


    nombre_existente = tblUnidades.objects.filter(Descripcion=descripcion).exclude(ID=id).exists()
    if nombre_existente:
        messages.error(request, f'La unidad de medida "{descripcion}" ya ha sido registrado anteriormente.')
        IDNumber = int(id)
        return redirect('subtabla:E_Unidad_Medida', IDNumber)
    else:
        unidades = tblUnidades.objects.get(ID=id)
        unidades.Descripcion = descripcion
        unidades.Abreviacion = abreviacion
        unidades.save()

        messages.success(request, f'La unidad de medida "{descripcion}" se ha actualizado exitosamente.')
    return redirect('subtabla:T_Unidad_Medida')