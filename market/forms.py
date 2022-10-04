from market.models import Personal
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