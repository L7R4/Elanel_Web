from asyncio.windows_events import NULL
from random import choices
from django.urls import reverse
from email.policy import default
from django.db import models
# from django.template.defaultfilters import slugify
from django.utils.text import slugify

class Moto(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    descripcion = models.TextField(blank=True)
    modelo = models.CharField(max_length=80, blank = True)
    marca = models.CharField(max_length=80, blank = True)
    forma_de_pago = models.CharField(max_length= 255)
    imagen_portada = models.ImageField(upload_to="images/motos/", default=None)
    usado = models.BooleanField()
    cuotas = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.nombre)
        super(Moto, self).save(*args, **kwargs)
class ImagenMoto(models.Model):
    imagen = models.ImageField(upload_to ="images/motos/")
    producto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name= "imagenes", db_constraint=False)



class Electrodomestico(models.Model):
    combos = (
        ('cocina', 'cocina'),
        ('gamer', 'gamer'),
        ('musica', 'musica'),
        ('tv', 'tv'),
    )
    combo = models.CharField(max_length=100, choices=combos)
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,primary_key=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    descripcion = models.TextField(blank=True)
    marca = models.CharField(max_length=80, blank = True)
    forma_de_pago = models.CharField(max_length= 255)
    imagen_portada = models.ImageField(upload_to="images/motos/", default=None)
    usado = models.BooleanField()
    cuotas = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.nombre)
        super(Electrodomestico, self).save(*args, **kwargs)

class ImagenElectrodomestico(models.Model):
    imagen = models.ImageField(upload_to ="images/electrodomesticos/")
    producto = models.ForeignKey(Electrodomestico, on_delete=models.CASCADE, related_name= "imagenes", db_constraint=False)



class SolucionDineraria(models.Model):
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    cuotas = models.PositiveSmallIntegerField()
    monto_cuota = models.DecimalField(max_digits=15, decimal_places=2)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return str(self.monto)

    

class BeneficioParaCliente(models.Model):
    fecha = models.DateTimeField(auto_now_add = True)
    nombre_completo = models.CharField(max_length= 120)
    email = models.EmailField(max_length=200) 
    servicio = models.CharField(max_length=254)
    num_telefono = models.CharField(max_length=15)


class Cliente(models.Model):
    nombre_completo = models.CharField(max_length= 120, default="")
    dni = models.CharField(max_length=8)
    provincia = models.CharField(max_length=50)  
    localidad = models.CharField(max_length=50)  
    email = models.EmailField(max_length=200) 
    objetivo = models.CharField(max_length=254)
    num_telefono = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nombre_completo
class Personal(models.Model):
    nombre_completo = models.CharField(max_length= 120, default="")
    email = models.EmailField(max_length=200) 
    num_telefono = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add = True)
    cv = models.FileField(upload_to="archivos/cv/", default=None, blank=False)

class Post(models.Model):
    titulo = models.CharField(max_length=60,blank=True)
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField()
    fecha_limite = models.DateTimeField()
    imagen_portada = models.ImageField(upload_to= "images/posts", default=None)
class PostImagenes(models.Model):
    imagen = models.ImageField(upload_to="images/posts", default=None)
    descripcion = models.CharField(max_length=255, blank=True)
    producto = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= "imagenes")








    


