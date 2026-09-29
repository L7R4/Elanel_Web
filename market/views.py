import json
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View
from django.views import generic
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from market.models import Electrodomestico,ImagenMoto,ImagenElectrodomestico, Moto, Personal
from .forms import FormPersonal
import os


   

class Categorias(generic.ListView):
    template_name = "templates_categorias/categorias.html"
    
    def get_queryset(self):
        return None

def is_valid_query(param):
        return param != "" and param is not None


def nombre_archivo(archivo):
    """Nombre del archivo subido, o cadena vacía si no hay archivo."""
    return os.path.basename(archivo.name) if archivo else ""


def marcas_para_filtro(marcas):
    """Lista de (valor, etiqueta) sin duplicados; la etiqueta respeta cómo se cargó la marca."""
    unicas = {}
    for m in marcas:
        if m and m.strip():
            unicas.setdefault(m.strip().lower(), m.strip())
    return sorted(unicas.items())

class CategoriaMotos(generic.ListView):
    template_name = "templates_categorias/categorias_motos.html"
    model = Moto
    context_object_name ="motos"

    def get_queryset(self):
        qs = super().get_queryset().exclude(imagen_portada="").order_by("usado", "marca", "nombre")
        marca = self.request.GET.get("marca")
        status = self.request.GET.get("status")
        if is_valid_query(marca):
            qs = qs.filter(marca__iexact = marca)
        if status in ("True", "False"):
            qs = qs.filter(usado = status == "True")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        marcas = Moto.objects.exclude(imagen_portada="").values_list("marca", flat=True)
        context["marcas"] = marcas_para_filtro(marcas)
        context["marca_actual"] = (self.request.GET.get("marca") or "").lower()
        status = self.request.GET.get("status")
        context["status_actual"] = status if status in ("True", "False") else ""
        return context
    

class DetalleMoto(generic.DetailView):
    model = Moto
    template_name = "templates_categorias/detalle_moto.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        moto = self.object
        context["imagenes"] = ImagenMoto.objects.filter(producto = moto)
        context["ficha_tecnica"] = nombre_archivo(moto.ficha_tecnica)
        context["relacionados"] = (Moto.objects.exclude(pk = moto.pk)
                                   .exclude(imagen_portada = "")
                                   .filter(usado = moto.usado)[:4])
        return context



TIPOS_ELECTRO = (
    ("cocina", "Cocina"),
    ("tecnologia", "Tecnología"),
    ("dormitorio", "Dormitorio"),
    ("living", "Living"),
    ("hogar", "Hogar"),
)


class CategoriaElectrodemesticos(generic.ListView):
    model = Electrodomestico
    template_name = "templates_categorias/categorias_electrodomesticos.html"
    context_object_name ="electrodomesticos"

    def get_queryset(self):
        qs = super().get_queryset().exclude(imagen_portada="").order_by("combo", "marca", "nombre")
        combo = self.request.GET.get("combo")
        marca = self.request.GET.get("marca")
        if is_valid_query(combo):
            qs = qs.filter(combo = combo)
        if is_valid_query(marca):
            qs = qs.filter(marca__iexact = marca)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        disponibles = Electrodomestico.objects.exclude(imagen_portada="")
        usados = set(disponibles.values_list("combo", flat=True))
        context["tipos"] = [(valor, nombre) for valor, nombre in TIPOS_ELECTRO if valor in usados]
        marcas = disponibles.values_list("marca", flat=True)
        context["marcas"] = marcas_para_filtro(marcas)
        combo = self.request.GET.get("combo") or ""
        context["tipo_actual"] = combo if combo in usados else ""
        context["marca_actual"] = (self.request.GET.get("marca") or "").lower()
        return context



class DetalleElec(generic.DetailView):
    model = Electrodomestico
    template_name = "templates_categorias/detalle_electrodomesticos.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        electro = self.object
        context["imagenes"] = ImagenElectrodomestico.objects.filter(producto = electro)
        context["ficha_tecnica"] = nombre_archivo(electro.ficha_tecnica)
        context["tipo"] = dict(TIPOS_ELECTRO).get(electro.combo, "")
        context["relacionados"] = (Electrodomestico.objects.exclude(pk = electro.pk)
                                   .exclude(imagen_portada = "")
                                   .filter(combo = electro.combo)[:4])
        return context



class CategoriaSolucionesDinerarias(generic.TemplateView):
    template_name = "templates_categorias/categorias_soluciones_dinerarias.html"


class TrabajaConNosotros(View):
    template_name="trabaja_con_nosotros.html"

    def post(self,request,*args, **kwargs):
        form = FormPersonal()
        if request.method == "POST":
            print("Entre POST")
            form = FormPersonal(request.POST, request.FILES)
            if form.is_valid():
                print("es valido")
                personal = Personal()
                personal.nombre_completo = form.cleaned_data['nombre_completo']
                personal.email = form.cleaned_data['email']
                personal.num_telefono = form.cleaned_data['num_telefono']
                personal.cv = form.cleaned_data['cv']
                personal.save()
            else:
                print(form)
                message_error = {"message": "No valido"}
                data = json.dumps(message_error)
                return HttpResponse(data,"application/json")

        return(render(request,self.template_name))

    def get(self, request, *args, **kwargs):
        return(render(request,self.template_name))




