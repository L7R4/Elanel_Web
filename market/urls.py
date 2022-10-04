from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from market.views import  TrabajaConNosotros, CategoriaMotos,CategoriaElectrodemesticos,CategoriaSolucionesDinerarias, CategoriaBeneficiosCliente, Categorias,DetalleMoto
app_name="market"

urlpatterns = [
    path("categorias/",Categorias.as_view(),name="categorias"),
    path("categorias/motos/",CategoriaMotos.as_view(),name="motos"),

    path("categorias/motos/<slug:slug>/", DetalleMoto.as_view(),name="moto", ),
    path("categorias/motos/", CategoriaMotos.as_view(), name="clear"),
    path("categorias/elec/",CategoriaElectrodemesticos.as_view(), name="electrodomesticos"),
    path("categorias/beneficios/", CategoriaBeneficiosCliente.as_view(), name="beneficios"),
    path("categorias/soluciones_dinerarias/", CategoriaSolucionesDinerarias.as_view(),name="soluciones_dinerarias"),
    path("trabaja_con_nosotros/", TrabajaConNosotros.as_view(),name="trabaja"),
]
# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
