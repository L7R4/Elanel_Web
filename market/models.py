from random import choices
from django.urls import reverse
from email.policy import default
from django.db import models
# from django.template.defaultfilters import slugify
from django.utils.text import slugify
from django_quill.fields import QuillField
from django.core.validators import RegexValidator
import datetime


class Moto(models.Model):
    servicios = (
        ('Basico', 'Basico'),
        ('Estandar', 'Estandar'),
        ('Premium', 'Premium')
        )
    cuotas = (
        ('24','24'),
        ('30','30'),
        ('48','48'),
        ('60','60'),
    )

    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    modelo = models.CharField(max_length=80, blank = True)
    kilometros = models.IntegerField(blank=True, null=True)
    año = models.IntegerField(blank=True,null=True)
    marca = models.CharField(max_length=80, blank = True)
    forma_de_pago = models.CharField(max_length= 255, blank=True,null=True)
    descripcion = QuillField(blank=True,null=True)
    imagen_portada = models.ImageField(upload_to="images/motos/", default=None) 
    servicio = models.CharField(choices=servicios, max_length=50, default="Basico", blank=True,null=True)
    monto_servicio_por_couta = models.FloatField(blank=True,null=True)

    usado = models.BooleanField()
    cuota = models.CharField(max_length=2, choices=cuotas,default='24')
    ficha_tecnica = models.FileField(upload_to="f_tecnicas/motos/",default=None,blank=True,null=True)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.nombre)
        super(Moto, self).save(*args, **kwargs)
class ImagenMoto(models.Model):
    imagen = models.ImageField(upload_to ="images/motos/")
    producto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name= "imagenes", db_constraint=False)



class Electrodomestico(models.Model):
    cuotas = (
        ('24','24'),
        ('30','30'),
        ('48','48'),
        ('60','60'),
    )
    servicios = (
        ('Basico', 'Basico'),
        ('Estandar', 'Estandar'),
        ('Premium', 'Premium')
        )
    combos = (
        ('cocina', 'cocina'),
        ('tecnologia', 'tecnologia'),
        ('dormitorio', 'dormitorio'),
        ('living', 'living'),
        ('hogar', 'hogar'),
    )
    combo = models.CharField(max_length=100, choices=combos)
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,primary_key=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    descripcion = QuillField(blank=True,null=True)
    marca = models.CharField(max_length=80,blank=True,null=True)
    forma_de_pago = models.CharField(max_length= 255 ,blank=True,null=True)
    imagen_portada = models.ImageField(upload_to="images/electrodomesticos/", default=None)
    # usado = models.BooleanField()
    cuota = models.CharField(max_length=2, choices=cuotas,default='24')
    servicio = models.CharField(choices=servicios, max_length=50, default="Basico",blank=True,null=True)
    monto_servicio_por_couta = models.FloatField(blank=True,null=True)
    ficha_tecnica = models.FileField(upload_to="f_tecnicas/electrodomesticos/",default=None,blank=True,null=True)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.nombre)
        super(Electrodomestico, self).save(*args, **kwargs)

class ImagenElectrodomestico(models.Model) :
    imagen = models.ImageField(upload_to ="images/electrodomesticos/")
    producto = models.ForeignKey(Electrodomestico, on_delete=models.CASCADE, related_name= "imagenes", db_constraint=False)



class SolucionDineraria(models.Model):  
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    descripcion = QuillField(blank=True,null=True)

    def __str__(self):
        return str(self.monto)

    

class BeneficioParaCliente(models.Model):
    fecha = models.DateTimeField(auto_now_add = True)
    nombre_completo = models.CharField(max_length= 120,validators=[RegexValidator(r'^[a-zA-ZñÑ ]+$', 'Ingrese solo letras')])
    email = models.EmailField(max_length=200) 
    servicio = models.CharField(max_length=254)
    producto = models.CharField(max_length=80, default="")
    monto = models.FloatField(validators=[RegexValidator(r'^\d+(\.\d+)?$', 'Ingrese un número válido')])
    num_telefono = models.CharField(max_length=10,validators=[RegexValidator(r'^\d+(\.\d+)?$', 'Ingrese un número válido')])
    
    def __str__(self):
        return self.email + ' // ' + self.servicio


class Cliente(models.Model):
    nombre_completo = models.CharField(max_length= 120, default="", validators=[RegexValidator(r'^[a-zA-ZñÑ ]+$', 'Ingrese solo letras')])
    dni = models.CharField(max_length=8, blank=True, null=True, validators=[RegexValidator(r'^\d+(\.\d+)?$', 'Ingrese un número válido')])
    provincia = models.CharField(max_length=50,blank=True, null=True, validators=[RegexValidator(r'^[a-zA-ZñÑ ]+$', 'Ingrese solo letras')])  
    localidad = models.CharField(max_length=50,blank=True, null=True, validators=[RegexValidator(r'^[a-zA-ZñÑ ]+$', 'Ingrese solo letras')])  
    email = models.EmailField(max_length=200,blank=True, null=True) 
    objetivo = models.CharField(max_length=254)
    num_telefono = models.CharField(blank=True, null=True, validators=[RegexValidator(r'^\d+(\.\d+)?$', 'Ingrese un número válido')], max_length=10)
    fecha = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nombre_completo

class Personal(models.Model):
    nombre_completo = models.CharField(max_length= 120, default="", validators=[RegexValidator(r'^[a-zA-ZñÑ ]+$', 'Ingrese solo letras')])
    email = models.EmailField(max_length=200) 
    num_telefono = models.CharField(max_length=10, validators=[RegexValidator(r'^\d+(\.\d+)?$', 'Ingrese un número válido')])
    fecha = models.DateTimeField(auto_now_add = True)
    cv = models.FileField(upload_to="archivos/cv/", default=None, blank=False)

class Post(models.Model):
    postImage_celular = models.ImageField("Post de celular",upload_to= "images/posts", default=None, blank=True,null=True)
    postImage_computadora = models.ImageField("Post de computadora",upload_to= "images/posts", default=None,blank=True,null=True)


class NumAdjudicado(models.Model):
    year = datetime.date.today().year

    meses = (
        ('Enero', 'Enero'),
        ('Febrero', 'Febrero'),
        ('Marzo', 'Marzo'),
        ('Abril', 'Abril'),
        ('Mayo', 'Mayo'),
        ('Junio', 'Junio'),
        ('Julio', 'Julio'),
        ('Agosto', 'Agosto'),
        ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'),
        ('Noviembre', 'Noviembre'),
        ('Diciembre', 'Diciembre')
    )

    numero = models.PositiveIntegerField()
    mes = models.CharField(choices=meses, max_length=50, default='Enero')
    año = models.PositiveIntegerField(default=year)

    def __str__(self):
        return 'Numero: ' + str(self.numero) + ' de ' + self.mes + ' del ' + str(self.año)







    


