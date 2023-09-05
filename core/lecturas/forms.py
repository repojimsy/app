from django import forms
from .models import Lectura, Medidor
from .forms import *
from django.forms import ModelForm


# class LecturaForm(ModelForm):
#     class Meta:
#         model = Lectura
#         fields = ['medidor', 'fotografia','usuario', 'valor_lectura']

class LecturaForm(ModelForm):
    class Meta:
        model = Lectura
        fields = ['medidor', 'fotografia', 'usuario', 'valor_lectura']
    


#         fotografia = forms.ImageField(
#         required=False,  # Hacer que el campo sea opcional
#         widget=forms.FileInput(attrs={'accept': 'images/*'}), 
#         )

#         widget = {
#             'medidor' : forms.Select(attrs={'class': 'form-control'}),
#             'fotografia' : forms.Select(attrs={'class': 'form-control'}),
#             'usuario' : forms.Select(attrs={'class': 'form-control'}),
#             'valor_lectura' : forms.Select(attrs={'class': 'form-control'}),
#         }

# class LecturaForm(ModelForm):
#     class Meta:
#         model = Lectura
#         fields = ['medidor']
#         labels = {
#             'medidor':'Suministro'
#         }
#         widgets = {
#             'medidor': Select(
#                 attrs={
#                     'class':'form-control',
#                     'placeholder':'Ingrese un suministro',
#                     'autocomplete':'off',
#                 }
#             )
#         }



class UploadExcelForm(forms.Form):
    excel_file = forms.FileField(label='Seleccionar archivo Excel')
    





           

