from django.contrib import admin
from .models import BeneficioParaCliente, Cliente, Electrodomestico, ImagenMoto, ImagenElectrodomestico, Moto, SolucionDineraria, Personal, Post, NumAdjudicado
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente

class BeneficioParaClienteResource(resources.ModelResource):
    class Meta:
        model = BeneficioParaCliente

class PersonalResource(resources.ModelResource):
    class Meta:
        model = Personal

@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin):
    list_display= ["nombre_completo","email", "provincia","objetivo","fecha"]
    search_fields = ["nombre_completo","provincia","objetivo"]
    list_filter=["fecha"]
    list_per_page = 20
    resource_class = ClienteResource

@admin.register(Personal)
class PersonalAdmin(ImportExportModelAdmin):
    list_display= ["nombre_completo","email","cv","fecha"]
    search_fields = ["nombre_completo","fecha"]
    list_filter=["fecha"]
    resource_class = PersonalResource

class ImagenMotoAdmin(admin.TabularInline):
    extra = 3
    model = ImagenMoto

@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display= ["nombre", "precio", "modelo","marca", "usado"]
    search_fields = ["nombre","marca"]
    list_filter=["usado", "marca"]
    list_editable = ["precio", "usado"]
    inlines = [ImagenMotoAdmin]
    prepopulated_fields = {'slug': ['nombre']}

class ImagenElectrodomesticoAdmin(admin.TabularInline):
    extra = 3
    model = ImagenElectrodomestico

@admin.register(Electrodomestico)
class ElectrodomesticoAdmin(admin.ModelAdmin):
    list_display= ["nombre", "precio","combo"]
    search_fields = ["nombre","marca"]
    list_filter=["marca","combo"]
    list_editable = ["precio"]
    inlines = [ImagenElectrodomesticoAdmin]
    prepopulated_fields = {'slug': ['nombre']}

@admin.register(BeneficioParaCliente)
class BeneficioParaClienteAdmin(ImportExportModelAdmin):
    list_display =["servicio","producto","fecha"]
    list_filter=["servicio","fecha"]
    search_fields = ["producto"]
    resource_class = BeneficioParaClienteResource

admin.site.register(SolucionDineraria)
admin.site.register(Post)
admin.site.register(NumAdjudicado)
