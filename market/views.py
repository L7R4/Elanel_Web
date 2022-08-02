from configparser import NoSectionError
from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from market.models import Post


class CategoriaMotos(generic.ListView):
    template_name = "categoria-motos.html"
    
    def get_queryset(self):
        return None


class CategoriaElectrodemesticos(generic.ListView):
    template_name = "categoria-electrodomesticos.html"

    def get_queryset(self):
        return None


class CategoriaSolucionesDinerarias(generic.ListView):
    template_name = "categoria-soluciones-dinerarias.html"

    def get_queryset(self):
        return None


class CategoriaBeneficiosCliente(generic.ListView):
    template_name = "categoria-beneficios-cliente.html"

    def get_queryset(self):
        return None


