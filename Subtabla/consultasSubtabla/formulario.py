from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from Aplicacion.views import servicioActivo

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FORMUALRIO DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------
def formularioEstatus(request):
    ServiciosWeb = servicioActivo() 
    ultimo_id = tblEstatus.objects.order_by('-ID').first()
    if ultimo_id:
        ultimo_folio = ultimo_id.ID + 1
    else:
        ultimo_folio = 1
    
    return render(request, 'Estatus/form.html',{
    'ultimo_folio': ultimo_folio, 'ServiciosWeb':ServiciosWeb})

def formularioUnidadMedida(request):
    ServiciosWeb = servicioActivo() 
    ultimo_id = tblUnidades.objects.order_by('-ID').first()
    if ultimo_id:
        ultimo_folio = ultimo_id.ID + 1
    else:
        ultimo_folio = 1
    
    return render(request, 'UnidadMedida/form.html',{
    'ultimo_folio': ultimo_folio, 'ServiciosWeb':ServiciosWeb})

