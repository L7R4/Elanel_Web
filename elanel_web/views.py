from django.views.generic import View
from django.shortcuts import render,redirect, HttpResponseRedirect
from market.models import Post, Moto, NumAdjudicado
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
        motos_slider = Moto.objects.all()[5:10]
        nums_adjudicados = NumAdjudicado.objects.all()
        for post in posts:
            print(post.postImage_computadora == "")
        context = {
            "posts": posts,
            "motos_slider": motos_slider,
            "nums_adjudicados": nums_adjudicados,
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

