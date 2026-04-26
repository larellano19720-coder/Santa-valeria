from django.urls import path
from . import views
from Descargas.Descarga.EXCEL import excel



urlpatterns = [
       # PDF
    path('Cargamento_tolva/', views.cargamento_tolva, name="PDF_Tolva"), # PDF para tolvasx
    # path('Descarga_PDF_Entrada_Bascula/', views.entradaBasculas, name="PDF_Entrada_Bascula"), # PDF entrada productosx
    # path('Descarga_PDF_Salida_Bascula/', views.salidaBasculas, name="PDF_Salida_Bascula"), # PDF salida productosx
    # path('Descarga_PDF_Entrada_Materia_Prima/', views.entradaMateriaPrima, name="PDF_Entrada_Materia_Prima"), # PDF entrada materias primasx
    # path('Descarga_PDF_Salida_Materia_Prima/', views.salidaMateriaPrima, name="PDF_Salida_Materia_Prima"), # PDF salida materias primasx
    # path('Descarga_PDF_Movimiento_Animales/', views.movimientoAnimales, name="PDF_Movimientos_Animales"), # PDF salida materias primasx

    path('Descarga_PDF_Ordenes_Servidos/', views.ordenServidoPDF, name="PDF_Orden_Servidos"), # PDF movimientos servidosx

    # PDF Reportes
    path('Descarga_PDF_Reporte_Movimientos_Servidos/', views.reporteMovimientoServidos, name="PDF_Reportes_Mov_Servidos"), # PDF movimientos servidosx
    # path('Descarga_PDF_Reporte_Liquidacion_Servidos/', views.reporteLiquidacionServidos, name="PDF_Reportes_Liq_Servidos"), # PDF liquidacion servidosx
    # path('Descarga_PDF_Reporte_Entrada_Materia_Prima/', views.reporteEntradaMateriaPrima, name="PDF_Reportes_Entrada_Materia_Prima"), # PDF movimiento entrada materias primasx
    # path('Descarga_PDF_Reporte_Salida_Materia_Prima/', views.reporteSalidaMateriaPrima, name="PDF_Reportes_Salida_Materia_Prima"), # PDF movimiento salida materias primasx
    # path('Descarga_PDF_Reporte_Movimientos_Animales/', views.reporteMovimientoAnimales, name="PDF_Reportes_Movimiento_Animales"), # PDF movimiento animalesx
    # path('Descarga_PDF_Reporte_Movimientos_Animales_Corral/', views.reporteMovimientoAnimalesCorral, name="PDF_Reportes_Movimiento_Animales_Corral"), # PDF movimiento aniamles corrales
    # path('Descarga_PDF_Reporte_Movimientos_Animales_Cliente/', views.reporteMovimientoAnimalesCliente, name="PDF_Reportes_Movimiento_Animales_Cliente"), # PDF movimiento animales clientex
    
    
    
    path('Descarga_EXCEL_Reporte_Movimientos_Servidos/', excel.ExportarServidoCorralExcel, name='exportar_servido_corral'),

]
