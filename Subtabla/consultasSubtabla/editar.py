from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from Aplicacion.views import servicioActivo
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< EDITAR FORMULARIO CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------
def editarEstatus(request, ID):
    ServiciosWeb = servicioActivo() 
    TEEstatus= tblEstatus.objects.get(ID=ID)
    return render(request, "Estatus/edit.html",{'TEEstatus': TEEstatus, 'ServiciosWeb':ServiciosWeb})


def editarUnidadMedida(request, ID):
    ServiciosWeb = servicioActivo() 
    TEUnidadMedida = tblUnidades.objects.get(ID=ID)
    return render(request, "UnidadMedida/edit.html",{'TEUnidadMedida': TEUnidadMedida, 'ServiciosWeb':ServiciosWeb})

