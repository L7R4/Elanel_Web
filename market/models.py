from distutils.command.upload import upload
from django.db import models
from django.forms import ImageField

class Producto:
    categorias = [
        ("motos", "Motos"),
        ("soluciones_dinerarias", "Soluciones dinerarias"),
        ("electrodomesticos", "Electrodomesticos"),
        ("usados", "Usados"),
        ("beneficios_para_clientes", "Beneficios para clientes"),
    ]
    titulo_de_categoria = models.CharField(max_length=30, choices= categorias)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    url_instagram = models.URLField(max_length=255, blank=True)
    url_facebook = models.URLField(max_length=255, blank=True)
    descripcion = models.TextField(blank=True)
    modelo = models.CharField(max_length=80, blank = True)
    marca = models.CharField(max_length=80, blank = True)
    especificaciones = models.TextField()
    forma_de_pago = models.CharField(max_length= 255)
    imagen_portada = ImageField(upload_to = "productos")
    usado = models.BooleanField()
    cuotas = models.IntegerField(max_length= 3)


    def __str__(self):
        return self.nombre

class ImagenProducto(models.model):
    imagen = models.ImageField(upload_to ="productos")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name= "imagenes")


class SolucionDineraria(models.Model):
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    cuotas = models.IntegerField(max_length=3)
    monto_cuota = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.monto


class Usuario(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    provincia = models.CharField(max_length=50)  
    localidad = models.CharField(max_length=50)  
    email = models.EmailField(max_length=200) 
    objetivo = models.CharField(max_length=254)
    num_telefono = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk + self.nombre + self.apellido


class Post(models.Model):
    titulo = models.CharField(max_length=60,blank=True)
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField()
    fecha_limite = models.DateTimeField()
    imagen_portada = models.ImageField(upload_to= "posts")



class PostImagenes(models.Model):
    imagen = models.ImageField(upload_to ="posts")
    descripcion = models.CharField(max_length=255, blank=True)
    producto = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= "imagenes")





    


