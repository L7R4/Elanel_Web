from django.contrib import admin
from .models import *

class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto

class ProductoAdmin(admin.ModelAdmin):
    list_display= ["nombre", "titulo_de_categoria", "modelo","marca"]
    list_editable= ["precio"]
    search_fields = ["nombre"]
    inlines = [ImagenProductoAdmin]


admin.site.register(Producto, ImagenProducto)
admin.site.register(SolucionDineraria)
admin.site.register(Usuario)
admin.site.register(Post, PostImagenes)
