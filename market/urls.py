from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from market.views import  TrabajaConNosotros, CategoriaMotos,DetalleElec,CategoriaElectrodemesticos,CategoriaSolucionesDinerarias, Categorias,DetalleMoto
app_name="market"

urlpatterns = [
    path("venta-directa/",Categorias.as_view(),name="categorias"),

    path("venta-directa/motos/",CategoriaMotos.as_view(),name="motos"),
    path("venta-directa/motos/<slug:slug>/", DetalleMoto.as_view(),name="moto"),
    path("venta-directa/motos/", CategoriaMotos.as_view(), name="clear"),


    path("venta-directa/electrodomesticos/",CategoriaElectrodemesticos.as_view(), name="electrodomesticos"),
    path("venta-directa/electrodomesticos/<slug:slug>/", DetalleElec.as_view(),name="electrodomestico"),
    path("venta-directa/electrodomesticos/", CategoriaElectrodemesticos.as_view(),name="clear_electrodomesticos"),


    path("soluciones/", CategoriaSolucionesDinerarias.as_view(),name="soluciones_dinerarias"),
    path("soluciones/<int:pk>/", RedirectView.as_view(url=reverse_lazy("market:soluciones_dinerarias"), permanent=True)),
    path("soluciones/", CategoriaSolucionesDinerarias.as_view(),name="clear_soluciones"),

    path("trabaja-con-nosotros/", TrabajaConNosotros.as_view(),name="trabaja"),
]
