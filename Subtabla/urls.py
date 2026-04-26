from django.urls import path
from . import views

from Subtabla.consultasSubtabla import actualizar, agregar, editar, mostrar, formulario

urlpatterns = [
    path('SubTabla_Estatus/', mostrar.TablaEstatus, name='T_Estatus'),
    path('SubTabla_Unidad_Medida/', mostrar.TablaUnidadMedida, name='T_Unidad_Medida'),
    
    # FORMULARIO SUBTABLAS
    path('Formulario_Estatus/', formulario.formularioEstatus, name='F_Estatus'),
    path('Formulario_Unidad_Medida/', formulario.formularioUnidadMedida, name='F_Unidad_Medida'),
    
    # FORMULARIO SUBTABLA
    path('Guardar_Estatus/', agregar.guardarEstatus, name="G_Estatus"),
    path('Guardar_Unidades/', agregar.guardarUnidadMedida, name="G_Unidad_Medida"),    

    # SUBTABLA EDITAR
    path('SubTabla_Estatus/Editar/<ID>', editar.editarEstatus, name="E_Estatus"),
    path('SubTabla_Unidad_Medida/Editar/<ID>', editar.editarUnidadMedida, name="E_Unidad_Medida"),   

    # ACTUALIZAR SUBTABLA
    path('ActualizarEstatus/', actualizar.actualizarEstatus, name="A_Estatus"),
    path('ActualizarUnidad/', actualizar.actualizarUnidadMedida, name="A_Unidad_Medida"),     
]
