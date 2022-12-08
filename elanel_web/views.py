from django.views.generic import View
from django.shortcuts import render,redirect, HttpResponseRedirect
from market.models import Post, Moto, NumAdjudicado
from django.views import generic
from .forms import FormIndex
from market.models import Cliente,Post

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

        return redirect('index')


    def get(self, request, *args, **kwargs):
        posts = Post.objects.all() 
        motos_slider = Moto.objects.all()[:5]
        num_adjudicado = NumAdjudicado.objects.all().last

        context = {
            "posts": posts,
            "motos_slider": motos_slider,
            "num_adjudicado": num_adjudicado,
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