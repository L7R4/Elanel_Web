import json
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from market.models import Electrodomestico,Cliente ,ImagenMoto,ImagenElectrodomestico, Post, Moto, Personal,BeneficioParaCliente,SolucionDineraria
from .forms import FormPersonal,FormBeneficios,FormDinero,FormMotos,FormElec
import os

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


    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        context ={}
        context["moto_images"] = ImagenMoto.objects.filter(producto = self.object)
        context["object"] = self.object
        try:
            model = Moto.objects.filter(slug = self.object.slug)
            archivo =os.path.split(str(model[0].ficha_tecnica))[1]
            context["ficha_tecnica"] = archivo
        except ValueError:
            print("No existe ficha tecnica")

        return render(request,self.template_name,context)
    
    def post(self,request,*args, **kwargs):
        self.object = self.get_object()
        form = FormMotos()
        if request.method == "POST":
            form = FormMotos(request.POST)
            if form.is_valid():
                print("es valido")
                form_moto = Cliente()
                form_moto.nombre_completo = form.cleaned_data['nombre_completo']
                form_moto.email = form.cleaned_data['email']
                form_moto.num_telefono = form.cleaned_data['num_telefono']
                form_moto.provincia = form.cleaned_data['provincia']
                form_moto.objetivo = form.cleaned_data['objetivo']
                form_moto.save()
            else:
                message_error = {"message": "No valido"}
                data = json.dumps(message_error)
                return HttpResponse(data,"application/json")

        return redirect('market:moto',self.object.slug)

    

        

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
            qs = qs.filter(cuota = cuota)
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

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        context ={}
        context["electrodomesticos_images"] = ImagenElectrodomestico.objects.filter(producto = self.object)
        context["object"] = self.object
        try:
            model = Moto.objects.filter(slug = self.object.slug)
            archivo =os.path.split(str(model[0].ficha_tecnica))[1]
            context["ficha_tecnica"] = archivo
        except:
            print("No existe ficha tecnica")

        return render(request,self.template_name,context)

    def post(self,request,*args, **kwargs):
        self.object = self.get_object()
        form = FormElec()
        if request.method == "POST":
            form = FormElec(request.POST)
            if form.is_valid():
                print("es valido")
                form_elec = Cliente()
                form_elec.nombre_completo = form.cleaned_data['nombre_completo']
                form_elec.email = form.cleaned_data['email']
                form_elec.num_telefono = form.cleaned_data['num_telefono']
                form_elec.provincia = form.cleaned_data['provincia']
                form_elec.objetivo = form.cleaned_data['objetivo']
                form_elec.save()
            else:
                message_error = {"message": "No valido"}
                data = json.dumps(message_error)
                return HttpResponse(data,"application/json")

        return redirect('market:electrodomestico',self.object.slug)


class CategoriaSolucionesDinerarias(generic.ListView):
    template_name = "templates_categorias/categorias_soluciones_dinerarias.html"
    model = SolucionDineraria
    context_object_name ="dineros"

    def get_queryset(self):
        qs = super().get_queryset()
        cuota = self.request.GET.get("cuota")
        if is_valid_query(cuota):
            qs = qs.filter(cuota = cuota)
        return qs

class DetalleSolucion(generic.DetailView):
    model = SolucionDineraria
    template_name = "templates_categorias/detalle_soluciones.html"

    def post(self,request,*args, **kwargs):
        self.object = self.get_object()
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
                solu_dine.provincia = form.cleaned_data['provincia']
                solu_dine.objetivo = form.cleaned_data['objetivo']
                solu_dine.save()
            else:
                message_error = {"message": "No valido"}
                data = json.dumps(message_error)
                return HttpResponse(data,"application/json")
        return redirect('market:solucione_detail',self.object.id)

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        context ={}
        context["object"] = self.object

        return render(request,self.template_name,context)


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
                beneficio.producto = form.cleaned_data['producto']
                beneficio.monto = form.cleaned_data['monto']
                beneficio.save()
            else:
                message_error = {"message": "No valido"}
                data = json.dumps(message_error)
                return HttpResponse(data,"application/json")

        return(render(request,self.template_name))

    def get(self, request, *args, **kwargs):
        context = {}
        productos_basico =  list(Moto.objects.filter(servicio="Basico")) + list(Electrodomestico.objects.filter(servicio="Basico"))
        productos_estandar = list(Moto.objects.filter(servicio="Estandar"))+ list(Electrodomestico.objects.filter(servicio="Estandar"))
        productos_premium = list(Moto.objects.filter(servicio="Premium"))+ list(Electrodomestico.objects.filter(servicio="Premium"))
        
        all_products = productos_estandar + productos_premium + productos_basico


        context["productos_basico"]  = productos_basico
        context["productos_estandar"]  = productos_estandar
        context["productos_premium"]  = productos_premium

        
        products_list =[]
        for product in all_products:
            data_product = {}
            data_product['nombre'] = product.nombre
            data_product['servicio'] = product.servicio
            if product.monto_servicio_por_couta == None:
                data_product['monto_mensual'] = 0
                data_product['monto_total'] = 0
            else:
                data_product['monto_mensual'] = product.monto_servicio_por_couta
                data_product['monto_total'] = product.monto_servicio_por_couta*12
            products_list.append(data_product)
        data = json.dumps(products_list)

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return HttpResponse(data, 'application/json')

        return(render(request,self.template_name,context))


    

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



