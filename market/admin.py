from django.contrib import admin
from .models import BeneficioParaCliente, ImagenProducto, PostImagenes, Producto, SolucionDineraria, Usuario, Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario


@admin.register(Usuario) #decorador que significa que al registrar producto lo extendemos con ProductoAdmin
class UsuarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ["nombre", "apellido","email", "provincia","objetivo", ]
    # search_fields = ["nombre"]
    # list_filter=["titulo_de_categoria"]
    # list_editable = ["precio"]
    resource_class = UsuarioResource


class ImagenProductoAdmin(admin.TabularInline):
    extra = 3
    model = ImagenProducto


@admin.register(Producto) #decorador que significa que al registrar producto lo extendemos con ProductoAdmin
class ProductoAdmin(admin.ModelAdmin):
    list_display= ["nombre", "precio","titulo_de_categoria", "modelo","marca"]
    search_fields = ["nombre"]
    list_filter=["titulo_de_categoria"]
    list_editable = ["precio"]
    inlines = [ImagenProductoAdmin]


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
