from configparser import NoSectionError
from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from market.models import Post


class Categorias(generic.ListView):
    template_name = "templates_categorias/categorias.html"
    
    def get_queryset(self):
        return None


class CategoriaMotos(generic.ListView):
    template_name = "templates_categorias/categorias_motos.html"
    
    def get_queryset(self):
        return None



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



class TrabajaConNosotros(generic.ListView):
    template_name = "trabaja_con_nosotros.html"
    
    def get_queryset(self):
        return None


