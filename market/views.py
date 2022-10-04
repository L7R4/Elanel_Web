from configparser import NoSectionError
from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from market.models import ImagenMoto, Post, Moto, Personal
from .forms import FormPersonal


class Categorias(generic.ListView):
    template_name = "templates_categorias/categorias.html"
    
    def get_queryset(self):
        return None

def is_valid_query(param):
        return param != "" and param is not None

class CategoriaMotos(generic.ListView):
    template_name = "templates_categorias/categorias_motos.html"
    model = Moto
    context_object_name ="motos"

    def get_queryset(self):
        qs = super().get_queryset()
        marca = self.request.GET.get("marca")
        status = self.request.GET.get("status")
        minimo = self.request.GET.get("minimo")
        maximo = self.request.GET.get("maximo")
        # status = self.request.GET.get("status")
        if is_valid_query(marca):
            qs = qs.filter(marca = marca)
        if is_valid_query(status):
            qs = qs.filter(usado = status)
        if is_valid_query(minimo):
            qs = qs.filter(precio__gte = minimo)
        if is_valid_query(maximo):
            qs = qs.filter(precio__lte = maximo)
            
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
    model = Moto
    template_name = "templates_categorias/detalle_moto.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["moto_single"] = Producto.objects.get(producto = self.kwargs['slug'])
        context["moto_images"] = ImagenMoto.objects.filter(producto = self.kwargs['slug'])
        return context
    

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

        return(render(request,self.template_name))

    def get(self, request, *args, **kwargs):
        return(render(request,self.template_name))

