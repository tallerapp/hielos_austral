from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Cabaña(models.Model):
    cabaña_id = models.AutoField(primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='cabañas/')
    
# hay que descargar una libreria pip install Pillow para trabajar con imagenes

class Reserva(models.Model):
    reserva_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cabaña = models.ForeignKey(Cabaña, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

class Disponibilidad(models.Model):
    fecha = models.DateField()
    cabaña = models.ForeignKey(Cabaña, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)

