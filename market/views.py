from configparser import NoSectionError
from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from market.models import ImagenProducto, Post, Producto


class Categorias(generic.ListView):
    template_name = "templates_categorias/categorias.html"
    
    def get_queryset(self):
        return None

def is_valid_query(param):
        return param != "" and param is not None

class CategoriaMotos(generic.ListView):
    template_name = "templates_categorias/categorias_motos.html"
    model = Producto
    context_object_name ="motos"

    

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["motos"] = Producto.objects.filter(titulo_de_categoria = "motos") 
    #     return context
    

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     marca = self.request.GET.get("marca")
    #     qs = Producto.objects.filter(titulo_de_categoria = "motos")
    #     if is_valid_query(marca):
    #         qs = qs.filter(marca__icontains = marca)
    #         print("hola")
    #         print(marca)
    #     context["motos"] = Producto.objects.filter(titulo_de_categoria = "motos") 
    #     return context

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(titulo_de_categoria = "motos")
        marca = self.request.GET.get("marca")
        # status = self.request.GET.get("status")
        if is_valid_query(marca):
            qs = qs.filter(marca = marca)
            print("hola")
            print(marca)
        # if is_valid_query(marca):
        #     pass
        
        return qs



class CategoriaElectrodemesticos(generic.ListView):
    template_name = "templates_categorias/categorias_electrodomesticos.html"

    def get_queryset(self):
        return None


class CategoriaSolucionesDinerarias(generic.ListView):
    template_name = "templates_categorias/categorias_soluciones_dinerarias.html"

    def get_queryset(self):
        return None


class CategoriaBeneficiosCliente(generic.ListView):
    template_name = "templates_categorias/categorias_beneficios_cliente.html"

    def get_queryset(self):
        return None

class DetalleMoto(generic.DetailView):
    model = Producto
    template_name = "templates_categorias/detalle_moto.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["moto_single"] = Producto.objects.get(producto = self.kwargs['slug'])
        context["moto_images"] = ImagenProducto.objects.filter(producto = self.kwargs['slug'])
        return context
    
    # def get_queryset(self):
    #     # original qs
    #     qs = super().get_queryset() 
    #     # filter by a variable captured from url, for example
    #     return qs.filter(producto = self.kwargs['slug'])
    



class TrabajaConNosotros(generic.ListView):
    template_name = "trabaja_con_nosotros.html"
    
    def get_queryset(self):
        return None


