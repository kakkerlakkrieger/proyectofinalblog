from django import forms
from django.db.models import fields
from django.db.models.base import Model
from bienvenido.models import Departamento, Empleado, Post

class FiltroDptos(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    numero = forms.IntegerField(required=False)

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ("nombre",)
    
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ("__all__")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("__all__")