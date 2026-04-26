from django.urls import path

from . import views
from Proceso.consultarProcesos import actualizar, agregar, editar, mostrar, formulario, dispositivos, cancelar


urlpatterns = [
    path('', views.homeProcesos, name='Inicio'),
    path('api/config/', dispositivos.obtener_comando, name='Dispositivos'),

    # DATOS DEL AREA DE SERVIDOS
    path('Solicitud_Servidos/', mostrar.TablaSolicitudServido, name='T_Solicitud_Servidos'),
    path('Orden_Servidos/', mostrar.TablaOrdenesServido, name='T_Orden_Servidos'),
    path('Corrales_Servidos/', mostrar.TablaServidoCorral, name='T_Corrales_Servidos'),
    path('Servidos_Manuales/', mostrar.TablaServidoManual, name='T_Servidos_manuales'),
    
        
    # DATOS DE LOS DATOS DE LA TOLVA
    path('Cargamento_Tolva/', mostrar.TablaCargamentoTolva, name='T_Cargamento_Tolva'),
    

    path('Formulario_Solicitud_Servido/',formulario.FormularioSolicitudServido, name='F_Solicitud_Servidos'),
    path('Formulario_Servidos_Manuales/',formulario.FormularioServidoAnimales, name='F_Servidos'),
    path('Replicar_Servidos/', formulario.FormularioReplicarServido, name='R_Servidos'),

    path('Guardar_Solicitud_Servidos/', agregar.guardarSolicitudServido, name="G_Solicitud_Servidos"),
    path('Guardar_Solicitud_Servidos/', agregar.guardarSolicitudServido, name="R_Solicitud_Servidos"),
    path('Guardar_Servidos_Manual/', agregar.guardarServidosManuales),

    path('Solicitud_Servidos/Editar/', editar.editarSolicitudServidos, name="E_Solicitud_Servidos"),
    path('Dato_Servidos_Manuales/Editar/<ID>', editar.editarServidosManuales),

    # ACTUALIZAR PROCESOS
    path('ActualizarServidorManual/', actualizar.actualizarServidosManual, name="A_Solicitud_Servidos"),
    path('Actualizar_Orden_Servidos/', actualizar.actualizarOrdenServidos, name="A_Orden_Servidos"),
    path('Agregar_Orden_Servidos/', actualizar.agregarSolicitudServido, name="AA_Orden_Servidos"),
    path('Actualizar_Orden_Visible/', actualizar.ordenVisible, name="ordenVisible"),
    path('ActualizarServidorManualCantidad/', actualizar.actualizarCantidadServidosManual, name="Cantidad_servidos_manuales"),
    path('ActualizarFormuladoManualCantidad/', actualizar.actualizarCantidadFormuladoManual, name="Cantidad_Formulado_manuales"),
    path('ActualizarServidosATolva/', actualizar.actualizarServidosATolva, name="A_Servidos_Tolva"),
    path('ActualizarFormuladoATolva/', actualizar.actualizarFormuladoATolva, name="A_Formulado_Tolva"),

    path('ActualizarCancelarServidosVehiculos/', actualizar.actualizarCancelarTolva, name="A_Pedido_Tolva"),
    path('ActualizarCancelarFormuladoVehiculos/', actualizar.actualizarCancelarFormulado, name="A_Pedido_Formulado"),
    
    path('Cancelar_Corral_Servidos/', cancelar.cancelarServidos, name="C_Corral_Servidos"),
    path('Cancelar_Orden_Servidos/', cancelar.cancelarOrdenServidos, name="C_Orden_Servidos"),
    path('Elimnar_Orden_Servidos/', cancelar.eliminarOrdenServidos, name="EM_Orden_Servidos"),
    
    ]
