import datetime
from django.views.generic import View
from django.shortcuts import render,redirect, HttpResponseRedirect
from market.models import Post, CuadroCobertura, Moto, Electrodomestico
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FormIndex
from market.models import Cliente,Post

import json

def page_error(request,exception):
    return render(request, 'pagenotfound.html')

class IndexView2(View):
    template_name="index.html"

    def post(self,request,*args, **kwargs):
        form = FormIndex()
        if request.method == "POST":
            form = FormIndex(request.POST)
            if form.is_valid():
                user = Cliente()
                user.nombre_completo = form.cleaned_data['nombre_completo']
                user.provincia = form.cleaned_data['provincia']
                user.localidad = form.cleaned_data['localidad']
                user.email = form.cleaned_data['email']
                user.objetivo = form.cleaned_data['objetivo']
                user.num_telefono = form.cleaned_data['num_telefono']
                user.save()
            else:
                message_error = {'meesage_error':"No enviado"}
                data = json.dumps(message_error)
                return HttpResponse(data, 'application/json')
        return redirect('index')


    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            "posts": posts,
            # "Destacados de este mes": primero los tildados como destacados en el admin,
            # y si hay menos de 4 se completa con los últimos cargados.
            "motos_venta": Moto.objects.exclude(imagen_portada="").order_by("-destacado", "usado", "-id")[:4],
            "electro_venta": Electrodomestico.objects.exclude(imagen_portada="").order_by("-destacado", "nombre")[:4],
            # Una foto real por categoría para el mosaico del hero (si no hay, se usa una imagen fija).
            "foto_moto_0km": Moto.objects.exclude(imagen_portada="").filter(usado=False).order_by("-id").first(),
            "foto_electro": Electrodomestico.objects.exclude(imagen_portada="").first(),
        }
        return(render(request,self.template_name,context))


class Servicios(generic.TemplateView):
    template_name = "servicios.html"


class Beneficios(generic.TemplateView):
    template_name = "beneficios.html"


class PreguntasFrecuentes(generic.TemplateView):
    template_name = "preguntas_frecuentes.html"


class Cobertura(View):
    template_name = "cobertura.html"

    def get(self, request, *args, **kwargs):
        publicados = CuadroCobertura.objects.filter(publicado=True, vigente_desde__lte=datetime.date.today())
        context = {
            "cuadro": publicados.first(),
            "anteriores": publicados[1:],
        }
        return(render(request,self.template_name,context))


class SobreNosotros(View):
    template_name = "sobre_nosotros.html"
    
    def get(self, request, *args, **kwargs):
        return(render(request,self.template_name))


class Contactanos(View):
    template_name = "contactanos.html"

    def get(self, request, *args, **kwargs):
        return(render(request,self.template_name))

class Privicidad(View):
    template_name = "privacidad.html"

    def get(self, request, *args, **kwargs):
        return(render(request,self.template_name))

