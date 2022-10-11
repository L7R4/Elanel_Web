from market.models import Personal,BeneficioParaCliente
from django import forms
class FormPersonal(forms.ModelForm):
    class Meta:
        model = Personal
        fields =[
            'nombre_completo',
            'email',
            'num_telefono',
            'cv',
        ]

class FormBeneficios(forms.ModelForm):
    class Meta:
        model = BeneficioParaCliente
        fields =[
            'nombre_completo',
            'email',
            'num_telefono',
            'servicio',
        ]