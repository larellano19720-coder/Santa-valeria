from django.shortcuts import render
from datetime import datetime, timedelta
# LLAMAR ARCHIVOS LOCALES
from django.db.models import Q
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db import connection
from Aplicacion.views import servicioActivo

def reporteServidosMovimientos(request):
    ServiciosWeb = servicioActivo()   
    FechaDeHoy = datetime.now().strftime('%Y-%m-%d')

    if request.method == 'POST':
        Fecha = request.POST.get('fecha1')
        Fecha2 = request.POST.get('fecha2')
        consulta_sql = """  
            SELECT  r.Porcentaje, c.Descripcion AS Corral, p.Descripcion AS Producto, r.CantidadAnimales, 
            r.CantidadSolicitada, r.Cantidad1, r.Cantidad2, (r.Cantidad1 + r.Cantidad2) AS TotalCantidad,
            ROUND((r.Cantidad1 + r.Cantidad2) / NULLIF(r.CantidadAnimales, 0), 2) AS PromedioPorAnimal, r.FechaSol, r.FechaServida1, r.FechaServida2
            FROM Aplicacion_tblrepartidor r
            LEFT JOIN Aplicacion_tblcorrales c ON r.IDCorral_id = c.ID
            LEFT JOIN Aplicacion_tblproductos p ON r.IDProducto_id = p.ID
            LEFT JOIN Aplicacion_tblestatus e ON r.IDEstatus_id = e.ID
            WHERE r.IDEstatus_id IN (10,11)
            AND DATE(r.FechaServida2) BETWEEN %s AND %s
            """
        with connection.cursor() as cursor:
            cursor.execute(consulta_sql, [Fecha, Fecha2])
            reportes = cursor.fetchall()

        return render(request, 'Reporte/Servidos/index.html', {'Fecha':Fecha,'Fecha2':Fecha2,'reportes': reportes, 'FechaDeHoy': FechaDeHoy, 'ServiciosWeb':ServiciosWeb})
            
    else:
        consulta_sql = """  
            SELECT  r.Porcentaje, c.Descripcion AS Corral, p.Descripcion AS Producto, r.CantidadAnimales, 
            r.CantidadSolicitada, r.Cantidad1, r.Cantidad2, (r.Cantidad1 + r.Cantidad2) AS TotalCantidad,
            ROUND((r.Cantidad1 + r.Cantidad2) / NULLIF(r.CantidadAnimales, 0), 2) AS PromedioPorAnimal, r.FechaSol, r.FechaServida1, r.FechaServida2
            FROM Aplicacion_tblrepartidor r
            LEFT JOIN Aplicacion_tblcorrales c ON r.IDCorral_id = c.ID
            LEFT JOIN Aplicacion_tblproductos p ON r.IDProducto_id = p.ID
            LEFT JOIN Aplicacion_tblestatus e ON r.IDEstatus_id = e.ID
            WHERE r.IDEstatus_id IN (10,11)
            AND DATE(r.FechaServida2) BETWEEN %s AND %s
        """

        with connection.cursor() as cursor:
            cursor.execute(consulta_sql, [FechaDeHoy, FechaDeHoy])
            reportes = cursor.fetchall()
    
        return render(request, 'Reporte/Servidos/index.html', {'reportes': reportes, 'FechaDeHoy': FechaDeHoy, 'ServiciosWeb':ServiciosWeb})
