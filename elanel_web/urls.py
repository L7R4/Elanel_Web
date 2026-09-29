from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from .views import IndexView2,SobreNosotros,Contactanos,page_error, Privicidad, Servicios, Cobertura, Beneficios, PreguntasFrecuentes

handler404 = page_error


def legacy(pattern_name):
    return RedirectView.as_view(pattern_name=pattern_name, permanent=True, query_string=True)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",IndexView2.as_view(), name = "index"),
    path("servicios/",Servicios.as_view(), name = "servicios"),
    path("cobertura/",Cobertura.as_view(), name = "cobertura"),
    path("beneficios/",Beneficios.as_view(), name = "beneficios"),
    path("preguntas-frecuentes/",PreguntasFrecuentes.as_view(), name = "faq"),
    path("nosotros/",SobreNosotros.as_view(), name = "nosotros"),
    path("contactanos/",Contactanos.as_view(), name = "contactanos"),
    path("politicas_de_privacidad/",Privicidad.as_view(), name = "privacidad"),
    path("notfound/", page_error,name="error"),
    path("", include("market.urls", namespace="market")),

    # Direcciones anteriores a la reorganización (se comparten en redes y Google)
    path("m/categorias/", legacy("market:categorias")),
    path("m/categorias/motos/", legacy("market:motos")),
    path("m/categorias/motos/<slug:slug>/", legacy("market:moto")),
    path("m/categorias/elec/", legacy("market:electrodomesticos")),
    path("m/categorias/elec/<slug:slug>/", legacy("market:electrodomestico")),
    path("m/categorias/beneficios/", legacy("servicios")),
    path("m/categorias/soluciones_dinerarias/", legacy("market:soluciones_dinerarias")),
    path("m/categorias/soluciones_dinerarias/<int:pk>/", RedirectView.as_view(url=reverse_lazy("market:soluciones_dinerarias"), permanent=True)),
    path("m/trabaja_con_nosotros/", legacy("market:trabaja")),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
