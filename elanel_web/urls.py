from unicodedata import name
from django import urls
from django.contrib import admin
from django.urls import path, include
# from .views import *
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls import handler404
from .views import IndexView2, SobreNosotros,Contactanos,page_error

# handler404 = page_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",IndexView2.as_view(), name = "index"),
    path("nosotros/",SobreNosotros.as_view(), name = "nosotros"),
    path("contactanos/",Contactanos.as_view(), name = "contactanos"),
    path("notfound/", page_error,name="error"),
    path("m/", include("market.urls", namespace="market")),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
