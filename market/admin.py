from django.contrib import admin
from .models import BeneficioParaCliente, Cliente, Electrodomestico, ImagenMoto, ImagenElectrodomestico, PostImagenes, Moto, SolucionDineraria, Personal, Post, NumAdjudicado
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente
class PersonalResource(resources.ModelResource):
    class Meta:
        model = Personal

@admin.register(Cliente) #decorador que significa que al registrar producto lo extendemos con ProductoAdmin
class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ["nombre_completo","email", "provincia","objetivo","fecha"]
    search_fields = ["nombre_completo","provincia","objetivo"]
    # list_filter=[("fecha",DateRangeFilter),"provincia"]
    list_filter=["fecha"]
    # list_editable = ["provincia"]
    # exclude = [""]
    list_per_page = 20
    resource_class = ClienteResource




@admin.register(Personal) 
class PersonalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ["nombre_completo","email", "num_telefono","cv","fecha"]
    search_fields = ["nombre_completo","fecha"]
    list_filter=["fecha"]
    resource_class = PersonalResource


class ImagenMotoAdmin(admin.TabularInline):
    extra = 3
    model = ImagenMoto

@admin.register(Moto) #decorador que significa que al registrar producto lo extendemos con ProductoAdmin
class MotoAdmin(admin.ModelAdmin):
    list_display= ["nombre", "precio", "modelo","marca", "usado"]
    search_fields = ["nombre","marca"]
    list_filter=["usado", "marca"]
    list_editable = ["precio", "usado"]
    inlines = [ImagenMotoAdmin]
    prepopulated_fields = { 'slug': ['nombre'] }

class ImagenElectrodomesticoAdmin(admin.TabularInline):
    extra = 3
    model = ImagenElectrodomestico

@admin.register(Electrodomestico) #decorador que significa que al registrar producto lo extendemos con ProductoAdmin
class ElectrodomesticoAdmin(admin.ModelAdmin):
    list_display= ["nombre", "precio","combo","marca"]
    search_fields = ["nombre","marca"]
    list_filter=["marca","combo"]
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


admin.site.register(SolucionDineraria)
admin.site.register(BeneficioParaCliente)
admin.site.register(NumAdjudicado)

