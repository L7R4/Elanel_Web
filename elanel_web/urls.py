from unicodedata import name
from django import urls
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",IndexView2.as_view(), name = "index"),
    path("nosotros/",SobreNosotros.as_view(), name = "nosotros"),
    path("contactanos/",Contactanos.as_view(), name = "contactanos"),
    path("m/", include("market.urls"), name="market"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
