from django.views.generic import View
from django.shortcuts import render
from market.models import Post, Producto
from django.views import generic

class IndexView(generic.ListView):
    model= Post
    template_name = "index.html"
    context_object_name = "posts"

    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motos'] = Producto.objects.filter(titulo_de_categoria = "motos")
        context["electrodomesticos"] = Producto.objects.filter(titulo_de_categoria= "electrodomesticos")
        return context
    
    


# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         context={
#             "posts": Post.objects.all()
#         }
#         return render(request, 'index.html', context)