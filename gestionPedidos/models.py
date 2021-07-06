from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="La Direccion")
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=7) 

    # def __str__(self):
    #     return 'Nombre: %s, Direccion: %s, Email: %s, Telefono: %s' %(self.nombre, self.direccion, self.email, self.telefono)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'Articulo: %s, Seccion: %s, Precio: %s' %(self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()