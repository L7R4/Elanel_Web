from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from market.views import CategoriaMotos, CategoriaElectrodemesticos,CategoriaSolucionesDinerarias,CategoriaBeneficiosCliente
app_name="market"

urlpatterns = [
    path("motos/",CategoriaMotos.as_view(),name="motos"),
    path("elec/",CategoriaElectrodemesticos.as_view(), name="electrodomesticos"),
    path("beneficios/", CategoriaBeneficiosCliente.as_view(), name="beneficios"),
    path("soluciones_dinerarias/", CategoriaSolucionesDinerarias.as_view(),name="soluciones_dinerarias")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
