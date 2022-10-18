from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View
from django.views import generic
from django.http import HttpResponseRedirect
from market.models import Electrodomestico,Cliente ,ImagenMoto,ImagenElectrodomestico, Post, Moto, Personal,BeneficioParaCliente,SolucionDineraria
from .forms import FormPersonal,FormBeneficios,FormDinero,FormMotos,FormElec


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
    

class DetalleMoto(generic.DetailView):
    model = Moto
    template_name = "templates_categorias/detalle_moto.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["moto_images"] = ImagenMoto.objects.filter(producto = self.object)
        return context
    
    def post(self,request,*args, **kwargs):
        form = FormMotos()
        if request.method == "POST":
            form = FormMotos(request.POST)
            if form.is_valid():
                print("es valido")
                form_moto = Cliente()
                form_moto.nombre_completo = form.cleaned_data['nombre_completo']
                form_moto.email = form.cleaned_data['email']
                form_moto.num_telefono = form.cleaned_data['num_telefono']
                form_moto.objetivo = form.cleaned_data['objetivo']
                form_moto.save()

        return redirect(request.META['HTTP_REFERER'])

    




class CategoriaElectrodemesticos(generic.ListView):
    model = Electrodomestico
    template_name = "templates_categorias/categorias_electrodomesticos.html"
    context_object_name ="electrodomesticos"

    def get_queryset(self):
        qs = super().get_queryset()
        cuota = self.request.GET.get("cuota")
        combo = self.request.GET.get("combo")
        minimo = self.request.GET.get("minimo")
        maximo = self.request.GET.get("maximo")
        if is_valid_query(cuota):
            qs = qs.filter(cuotas = cuota)
        if is_valid_query(combo):
            qs = qs.filter(combo = combo)
        if is_valid_query(minimo):
            qs = qs.filter(precio__gte = minimo)
        if is_valid_query(maximo):
            qs = qs.filter(precio__lte = maximo)
            
        return qs



class DetalleElec(generic.DetailView):
    model = Electrodomestico
    template_name = "templates_categorias/detalle_electrodomesticos.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["electrodomesticos_images"] = ImagenElectrodomestico.objects.filter(producto = self.object)
        return context
    
    def post(self,request,*args, **kwargs):
        form = FormElec()
        if request.method == "POST":
            form = FormElec(request.POST)
            if form.is_valid():
                print("es valido")
                form_elec = Cliente()
                form_elec.nombre_completo = form.cleaned_data['nombre_completo']
                form_elec.email = form.cleaned_data['email']
                form_elec.num_telefono = form.cleaned_data['num_telefono']
                form_elec.objetivo = form.cleaned_data['objetivo']
                form_elec.save()

        return redirect(request.META['HTTP_REFERER'])


class CategoriaSolucionesDinerarias(generic.ListView):
    template_name = "templates_categorias/categorias_soluciones_dinerarias.html"
    model = SolucionDineraria
    context_object_name ="dineros"

    def get_queryset(self):
        qs = super().get_queryset()
        cuota = self.request.GET.get("cuota")
        if is_valid_query(cuota):
            qs = qs.filter(cuotas = cuota)
        return qs

class DetalleSolucion(generic.DetailView):
    model = SolucionDineraria
    template_name = "templates_categorias/detalle_soluciones.html"

    def post(self,request,*args, **kwargs):
        form = FormDinero()
        if request.method == "POST":
            print("Entre POST")
            form = FormDinero(request.POST)
            if form.is_valid():
                print("es valido")
                solu_dine = Cliente()
                solu_dine.nombre_completo = form.cleaned_data['nombre_completo']
                solu_dine.email = form.cleaned_data['email']
                solu_dine.num_telefono = form.cleaned_data['num_telefono']
                solu_dine.objetivo = form.cleaned_data['objetivo']
                solu_dine.save()
            else:
                print(form)
        else:
            ("no entre al post")
        return(render(request,self.template_name))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoriaBeneficiosCliente(generic.ListView):
    template_name = "templates_categorias/categorias_beneficios_cliente.html"

    def post(self,request,*args, **kwargs):
        form = FormBeneficios()
        if request.method == "POST":
            print("Entre POST")
            form = FormBeneficios(request.POST)
            if form.is_valid():
                print("es valido")
                beneficio = BeneficioParaCliente()
                beneficio.nombre_completo = form.cleaned_data['nombre_completo']
                beneficio.email = form.cleaned_data['email']
                beneficio.num_telefono = form.cleaned_data['num_telefono']
                beneficio.servicio = form.cleaned_data['servicio']
                beneficio.save()
            else:
                print(form)

        return(render(request,self.template_name))

    def get(self, request, *args, **kwargs):
        return(render(request,self.template_name))


    

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

