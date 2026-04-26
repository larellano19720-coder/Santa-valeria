from django.urls import path
from . import views
from Catalogo.consultasCatalogo import actualizar, agregar, editar, mostrar, formulario


urlpatterns = [
   path('', views.homeCatalogos, name='Inicio'),
   
   # Tablas
   path('Operadores/', mostrar.TablaOperadores, name='T_Operador'),
   path('Materias_Primas/', mostrar.TablaMateriasPrimas, name='T_MateriaPrima'),
   path('Productos/', mostrar.TablaProductos, name='T_Producto'),
   path('Productos/Agregar/<ID>',mostrar.AgregarRecetas, name='AR_Producto'),   
   path('Corrales/', mostrar.TablaCorrales, name='T_Corral'),
   path('Tolvas/', mostrar.TablaTolva, name='T_Tolva'),
   
   # Formulario
   path('Formulario_Operadores/', formulario.FormualrioOperadores, name='F_Operador'),
   path('Formulario_Materias_Primas/', formulario.FormualrioMateriasPrimas, name='F_MateriaPrima'),

   path('Formulario_Productos/', formulario.FormualrioProductos, name='F_Producto'),
   path('Formulario_Corrales/', formulario.FormualrioCorrales, name='F_Corral'),
   path('Formulario_Tolvas/', formulario.FormualrioTolva, name='F_Tolva'),   
   
   # Guardar
   path('Guardar_Operadores/', agregar.guardarOperador, name='G_Operador'),
   path('Guardar_Materias_Primas/', agregar.guardarMateriasPrimas, name='G_MateriaPrima'),
   path('Guardar_Receta/', agregar.guardarRecetas, name='G_Receta'),
   path('Guardar_Productos/', agregar.guardarProductos, name='G_Producto'),
   path('Guardar_Corrales/', agregar.guardarCorrales, name='G_Corral'),
   path('Guardar_Tolvas/', agregar.guardarTolva, name='G_Tolva'),   

   #Editar
   path('Operadores/Editar/<ID>', editar.editarOperador, name='E_Operador'),
   path('Materias_Primas/Editar/<ID>', editar.editarMateriaPrima, name='E_MateriaPrima'),
   path('Productos/Editar/<ID>', editar.editarProducto, name='E_Producto'),
   path('Productos/Agregar/Editar/<ID>',editar.editarProductoReceta, name='ER_Producto'),
   path('Guardar_Receta/Editar/<ID>',editar.editarProductoReceta, name='ER_Producto'),
   path('Corrales/Editar/<ID>', editar.editarCorral, name='E_Corral'),
   path('Tolvas/Editar/<ID>', editar.editarTolva, name='E_Tolva'),   

   # Actualizar
   path('Actualizar_Operadores/', actualizar.actualizarOperador, name='A_Operador'),
   path('Actualizar_Materias_Primas/', actualizar.actualizarMateriaPrima, name='A_MateriaPrima'),
   path('Actualizar_Productos/', actualizar.actualizarProductos, name='A_Producto'),
   path('Actualizar_Recetas/', actualizar.actualizarRecetasProductos, name='A_Recetas'),
   path('Actualizar_Corrales/', actualizar.actualizarCorral, name='A_Corral'),
   path('Actualizar_Tolvas/', actualizar.actualizarTolva, name='A_Tolva'),   
]
