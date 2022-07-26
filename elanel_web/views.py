from django.views.generic import View
from django.shortcuts import render
from market.models import Post
from django.views import generic

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()


# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         context={
#             "posts": Post.objects.all()
#         }
#         return render(request, 'index.html', context)