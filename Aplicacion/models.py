from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission, AbstractBaseUser, BaseUserManager
    
class tblConfiguracion(models.Model):
    ID = models.AutoField(primary_key=True)
    Usuario = models.CharField(max_length=50, null=True)
    BaseDeDatos = models.CharField(max_length=50,null=True)
    FechaDescarga = models.DateTimeField(null=True)
    FechaActualizacion = models.DateTimeField(null=True)
    FolioSalMaquila = models.CharField(max_length=10, null=True)
    FolioRepServMov = models.CharField(max_length=10, null=True)
    FolioOrdenServ = models.CharField(max_length=10, null=True)
    
        
# -------------------------------------------------------SUBTABLAS-------------------------------------------------------
class tblEstatus(models.Model):
    ID = models.AutoField(primary_key=True)
    Clave = models.CharField(max_length=15, null=True)
    Descripcion = models.CharField(max_length=30,null=True)
    
class tblUnidades(models.Model):
    ID = models.AutoField(primary_key=True)
    Clave = models.CharField(max_length=15, null=True)
    Descripcion = models.CharField(max_length=30,null=True)
    Abreviacion = models.CharField(max_length=10,null=True)
    
    
# -------------------------------------------------------CATALOGOS-------------------------------------------------------
class tblOperadores(models.Model):
    ID = models.AutoField(primary_key=True)
    Clave = models.CharField(max_length=15, null=True)
    Descripcion = models.CharField(max_length=50, null=True)
    IDEstatus = models.ForeignKey(tblEstatus, on_delete=models.DO_NOTHING, null=True)

class tblMateriaPrima(models.Model):
    ID = models.AutoField(primary_key=True)
    Clave = models.CharField(max_length=15, null=True)
    Descripcion = models.CharField(max_length=50,null=True)
    IDEstatus = models.ForeignKey(tblEstatus, on_delete=models.DO_NOTHING, null=True)
    IDUnidadMedida = models.ForeignKey(tblUnidades, on_delete=models.DO_NOTHING, null=True)
    PrecioUnitario = models.FloatField(null=True)
    Merma = models.FloatField(null=True)
    
class tblProductos(models.Model):
    ID = models.AutoField(primary_key=True)
    Clave = models.CharField(max_length=15, null=True)
    Descripcion = models.CharField(max_length=50,null=True)
    IDEstatus = models.ForeignKey(tblEstatus, on_delete=models.DO_NOTHING, null=True)
    IDUnidadMedida = models.ForeignKey(tblUnidades, on_delete=models.DO_NOTHING, null=True)
    PrecioUnitario = models.FloatField(null=True)
    SeSirve = models.CharField(max_length=15, null=True)
    
class tblCorrales(models.Model):
    ID = models.AutoField(primary_key=True)
    Clave = models.CharField(max_length=15, null=True)
    Descripcion = models.CharField(max_length=50,null=True)
    IDEstatus = models.ForeignKey(tblEstatus, on_delete=models.DO_NOTHING, null=True)
    Fecha = models.DateTimeField(null=True)     
   
class tblTolva(models.Model):
    ID = models.AutoField(primary_key=True)
    Clave = models.CharField(max_length=15, null=True)
    Marca = models.CharField(max_length=15, null=True)
    Modelo = models.CharField(max_length=50, null=True)
    IDEstatus = models.ForeignKey(tblEstatus, on_delete=models.DO_NOTHING, null=True)
    IDProducto = models.ForeignKey(tblProductos, on_delete=models.DO_NOTHING, null=True)
    Capacidad = models.IntegerField(null=True)
    UdeM = models.ForeignKey(tblUnidades, on_delete=models.DO_NOTHING, null=True)
    Alias = models.CharField(max_length=50, null=True)
    
class tblRepartidor(models.Model):
    ID = models.AutoField(primary_key=True)
    Folio = models.CharField(max_length=15, null=True)
    IDCorral = models.ForeignKey(tblCorrales, on_delete=models.DO_NOTHING, null=True)
    IDProducto = models.ForeignKey(tblProductos, on_delete=models.DO_NOTHING, null=True)
    IDEstatus = models.ForeignKey(tblEstatus, on_delete=models.DO_NOTHING, null=True)
    IDTolva = models.ForeignKey(tblTolva, on_delete=models.DO_NOTHING, null=True)
    SeSirve = models.CharField(max_length=15, null=True)
    CantidadAnimales = models.IntegerField(null=True)
    CantidadSolicitada = models.IntegerField(null=True)
    Cantidad1 = models.IntegerField(null=True)
    Cantidad2 = models.IntegerField(null=True)
    Porcentaje = models.IntegerField(null=True)
    FechaSol = models.DateTimeField(null=True)
    FechaServida1 = models.DateTimeField(null=True)
    FechaServida2 = models.DateTimeField(null=True)
    IDLoteMezclado = models.IntegerField(null = True)

  
    
class tblFormulado(models.Model):
    ID = models.AutoField(primary_key=True)
    Folio = models.CharField(max_length=15, null=True)
    IDMateriaPrima = models.ForeignKey(tblMateriaPrima, on_delete=models.DO_NOTHING, null=True)
    IDProducto = models.ForeignKey(tblProductos, on_delete=models.DO_NOTHING, null=True)
    IDEstatus = models.ForeignKey(tblEstatus, on_delete=models.DO_NOTHING, null=True)
    IDTolva = models.ForeignKey(tblTolva, on_delete=models.DO_NOTHING, null=True)
    Proporcion = models.FloatField(null=True)
    CantidadSolicitada = models.CharField(max_length=15, null=True)
    CantidadServida = models.FloatField(null=True)
    Fecha = models.DateTimeField(max_length=150, null=True)
    FechaServida = models.DateTimeField(max_length=150, null=True)    
     
class tblReceta(models.Model):
    ID = models.AutoField(primary_key=True)
    Folio = models.CharField(max_length=15, null=True)
    IDMateriaPrima = models.ForeignKey(tblMateriaPrima, on_delete=models.DO_NOTHING, null=True)
    IDProductos = models.ForeignKey(tblProductos, on_delete=models.DO_NOTHING, null=True)
    Porcentaje = models.FloatField(null=True)
    Merma = models.FloatField(null=True)
    


class Control(models.Model):
    # Nombre del dispositivo
    ID = models.AutoField(primary_key=True)
    IDDispositivo = models.ForeignKey(tblTolva, on_delete=models.DO_NOTHING, null=True)
    Alias = models.CharField(max_length=100)
    Estatus = models.BooleanField(default=True)
    Token = models.CharField(max_length=100, unique=True)
    Movil = models.BooleanField(default=True)
    ComBau = models.IntegerField()
    
    IPBaseDatos = models.CharField(max_length=100, default="default")
    userMysql = models.CharField(max_length=100, default="default")
    passMysql = models.CharField(max_length=100, default="default")
    puerto = models.CharField(max_length=100, default="default")
    namebase = models.CharField(max_length=100, default="default")
    
    comando_pendiente = models.CharField(max_length=50, blank=True, null=True)
    ultima_conexion = models.DateTimeField(auto_now=True)
    
    
    
    
class tblServiciosWeb(models.Model):
    ID = models.AutoField(primary_key=True)
    Servicio = models.BooleanField(True, null=True)
    EstadoPago = models.BooleanField(True, null=True)
    FechaVencimiento = models.DateField(null=True)
    Notificacion = models.BooleanField(True, null=True)