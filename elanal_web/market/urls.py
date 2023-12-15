from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from market.views import  TrabajaConNosotros, CategoriaMotos,DetalleElec,DetalleSolucion,CategoriaElectrodemesticos,CategoriaSolucionesDinerarias, CategoriaBeneficiosCliente, Categorias,DetalleMoto
app_name="market"

urlpatterns = [
    path("categorias/",Categorias.as_view(),name="categorias"),

    path("categorias/motos/",CategoriaMotos.as_view(),name="motos"),
    path("categorias/motos/<slug:slug>/", DetalleMoto.as_view(),name="moto"),
    path("categorias/motos/", CategoriaMotos.as_view(), name="clear"),


    path("categorias/elec/",CategoriaElectrodemesticos.as_view(), name="electrodomesticos"),
    path("categorias/elec/<slug:slug>/", DetalleElec.as_view(),name="electrodomestico"),
    path("categorias/elec/", CategoriaElectrodemesticos.as_view(),name="clear_electrodomesticos"),

    path("categorias/beneficios/", CategoriaBeneficiosCliente.as_view(), name="beneficios"),
    

    path("categorias/soluciones_dinerarias/", CategoriaSolucionesDinerarias.as_view(),name="soluciones_dinerarias"),
    path("categorias/soluciones_dinerarias/<int:pk>/", DetalleSolucion.as_view(),name="solucione_detail"),
    path("categorias/soluciones_dinerarias/", CategoriaSolucionesDinerarias.as_view(),name="clear_soluciones"),

    path("trabaja_con_nosotros/", TrabajaConNosotros.as_view(),name="trabaja"),
]

