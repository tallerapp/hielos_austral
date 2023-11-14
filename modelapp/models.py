from django.db import models

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    password = models.CharField(max_length=100)


class Cabaña(models.Model):
    cabaña_id = models.AutoField(primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='cabañas/')
    
# hay que descargar una libreria pip install Pillow para trabajar con imagenes

class Reserva(models.Model):
    reserva_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabaña = models.ForeignKey(Cabaña, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

class Disponibilidad(models.Model):
    fecha = models.DateField()
    cabaña = models.ForeignKey(Cabaña, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)

