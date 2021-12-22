from django import forms
from .models import *
from django.contrib.auth.models import User
  
class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ('nombre', 'direccion')
 
  
class CuadroForm(forms.ModelForm):
    class Meta:
        model = Cuadro
        fields = ('nombre', 'galeria', 'autor', 'fecha_creacion', 'imagen')

class UserForm(forms.ModelForm):
     class Meta:
        model = User
        password = forms.CharField(widget=forms.PasswordInput)
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput
        }
