from django import forms
from market.models import Usuario

class FormIndex(forms.ModelForm):
    class Meta:
        model = Usuario
        fields =[
            'nombre_completo',
            'provincia',
            'localidad',
            'email',
            'objetivo',
            'num_telefono',
        ]