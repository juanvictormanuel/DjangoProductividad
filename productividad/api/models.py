from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Procedimientos(models.Model):
    idProcedimiento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    totalActividades = models.PositiveIntegerField()
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    activo = models.BooleanField(default=1)

    def __str__(self):
        return self.idUsuario.username

class Actividades(models.Model):
    idActividad = models.AutoField(primary_key=True)
    idProcedimientoFk = models.ForeignKey(Procedimientos,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fechaInicio = models.DateTimeField(default=now, verbose_name='Fecha Inicial')
    dias = models.PositiveIntegerField()
    fechaFin = models.DateTimeField(default=now, verbose_name="Fecha Final")
    jerarquia = models.PositiveIntegerField(null=True, blank=True)
    valor = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    completa = models.BooleanField(default=0)
    activo = models.BooleanField(default=1)

    def __str__(self):
        return self.nombre
