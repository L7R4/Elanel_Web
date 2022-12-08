from market.models import Personal,BeneficioParaCliente,Cliente
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
class FormDinero(forms.ModelForm):
    class Meta:
        model = Cliente
        fields =[
            'nombre_completo',
            'email',
            'num_telefono',
            'objetivo',
        ]
        
class FormMotos(forms.ModelForm):
    class Meta:
        model = Cliente
        fields =[
            'nombre_completo',
            'email',
            'num_telefono',
            'objetivo',
        ]
class FormElec(forms.ModelForm):
    class Meta:
        model = Cliente
        fields =[
            'nombre_completo',
            'email',
            'num_telefono',
            'objetivo',
        ]