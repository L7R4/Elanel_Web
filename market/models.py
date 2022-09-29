from asyncio.windows_events import NULL
from django.urls import reverse
from email.policy import default
from django.db import models
from django.template.defaultfilters import slugify

class Producto(models.Model):
    categorias = [
        ("motos", "Motos"),
        ("soluciones_dinerarias", "Soluciones dinerarias"),
        ("electrodomesticos", "Electrodomesticos"),
        ("usados", "Usados"),
        ("beneficios_para_clientes", "Beneficios para clientes"),
    ]
    titulo_de_categoria = models.CharField(max_length=30, choices= categorias)
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,primary_key=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    url_instagram = models.URLField(max_length=255, blank=True)
    url_facebook = models.URLField(max_length=255, blank=True)
    descripcion = models.TextField(blank=True)
    modelo = models.CharField(max_length=80, blank = True)
    marca = models.CharField(max_length=80, blank = True)
    especificaciones = models.TextField()
    forma_de_pago = models.CharField(max_length= 255)
    imagen_portada = models.ImageField(upload_to="images/productos/", default=None)
    usado = models.BooleanField()
    cuotas = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('nombre', 'slug')

    def __str__(self):
        return self.nombre
    

    def get_absolute_url(self):
        return reverse('market:moto', kwargs={'slug':self.slug})


class ImagenProducto(models.Model):
    imagen = models.ImageField(upload_to ="images/productos/")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name= "imagenes", db_constraint=False)


class SolucionDineraria(models.Model):
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    cuotas = models.PositiveSmallIntegerField()
    monto_cuota = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.monto


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


class BeneficioParaCliente(models.Model):
    asistencia = [
        ("tecnica_para_electrodomesticos", "Técnica para Electromesticos"),
        ("mecanica_de_motos", "Mecánica de Motos"),
    ]

    asistencia_titulo= models.CharField(max_length=50, choices=asistencia)
    nombre_tecnico = models.CharField(max_length = 50, default="")
    num_contacto = models.CharField(max_length= 11, default="")





    


