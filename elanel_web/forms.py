from django import forms
from market.models import Cliente


class FormIndex(forms.ModelForm):
    class Meta:
        model = Cliente
        fields =[
            'nombre_completo',
            'provincia',
            'localidad',
            'email',
            'objetivo',
            'num_telefono',
        ]

