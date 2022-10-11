from django.contrib import admin
from .models import BeneficioParaCliente, Cliente, Electrodomestico, ImagenMoto, ImagenElectrodomestico, PostImagenes, Moto, SolucionDineraria, Personal, Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente


@admin.register(Cliente) #decorador que significa que al registrar producto lo extendemos con ProductoAdmin
class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ["nombre_completo","email", "provincia","objetivo", ]
    # search_fields = ["nombre"]
    # list_filter=["titulo_de_categoria"]
    # list_editable = ["precio"]
    resource_class = ClienteResource

class PersonalResource(resources.ModelResource):
    class Meta:
        model = Personal


@admin.register(Personal) 
class PersonalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ["nombre_completo","email", "num_telefono","cv",]
    resource_class = PersonalResource


class ImagenMotoAdmin(admin.TabularInline):
    extra = 3
    model = ImagenMoto
@admin.register(Moto) #decorador que significa que al registrar producto lo extendemos con ProductoAdmin
class MotoAdmin(admin.ModelAdmin):
    list_display= ["nombre", "precio", "modelo","marca"]
    search_fields = ["nombre"]
    # list_filter=["titulo_de_categoria"]
    list_editable = ["precio"]
    inlines = [ImagenMotoAdmin]
    prepopulated_fields = { 'slug': ['nombre'] }

class ImagenElectrodomesticoAdmin(admin.TabularInline):
    extra = 3
    model = ImagenElectrodomestico

@admin.register(Electrodomestico) #decorador que significa que al registrar producto lo extendemos con ProductoAdmin
class ElectrodomesticoAdmin(admin.ModelAdmin):
    list_display= ["nombre", "precio","marca"]
    search_fields = ["nombre"]
    # list_filter=["titulo_de_categoria"]
    list_editable = ["precio"]
    inlines = [ImagenElectrodomesticoAdmin]
    prepopulated_fields = { 'slug': ['nombre'] }




class ImagenPostsAdmin(admin.TabularInline):
    extra = 3
    model = PostImagenes
@admin.register(Post)
class ProductoAdmin(admin.ModelAdmin):
    list_display= ["titulo","descripcion","imagen_portada"]
    inlines = [ImagenPostsAdmin]


# admin.site.register(Producto, ProductoAdmin)
admin.site.register(SolucionDineraria)
admin.site.register(BeneficioParaCliente)
# admin.site.register(Usuario)
# admin.site.register(Post) 
