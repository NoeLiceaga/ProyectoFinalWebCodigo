
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.contrib.auth import login, authenticate
from django.db.models import fields
from django.forms.widgets import Select

from main.models import CV, CategoriasTrabajo, Empresa, Genero, OfertaDeEmpleo


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta():
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]


class CvForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.id_usuario:
            self.fields['id_usuario'].widget.attrs.update({'readonly': True})

    class Meta:
        model = CV
        fields = [
            'id_usuario',
            'sexo',
            'profesion',
            'foto',
            'universidad_nombre',
            'universidad_inicio',
            'universidad_fin',
            'grado',
            'bachiller_nombre',
            'bachiller_inicio',
            'bachiller_fin',
            'empleo_anterior_empresa',
            'empleo_anterior_puesto',
            'empleo_anterior_inicio',
            'empleo_anterior_fin',
            'empleo_anterior2_empresa',
            'empleo_anterior2_puesto',
            'empleo_anterior2_inicio',
            'empleo_anterior2_fin',
            'descripcion',
            'idioma_extra',
            'idoma_porcentaje'
        ]
        widgets = {
            'universidad_inicio': forms.DateInput(format=('%d/%m/%Y'), attrs={'placeholder': 'Select a date', 'type': 'date'}),
            'universidad_fin': forms.DateInput(format=('%d/%m/%Y'), attrs={'placeholder': 'Select a date', 'type': 'date'}),
            'bachiller_inicio': forms.DateInput(format=('%d/%m/%Y'), attrs={'placeholder': 'Select a date', 'type': 'date'}),
            'bachiller_fin': forms.DateInput(format=('%d/%m/%Y'), attrs={'placeholder': 'Select a date', 'type': 'date'}),
            'empleo_anterior_inicio': forms.DateInput(format=('%d/%m/%Y'), attrs={'placeholder': 'Select a date', 'type': 'date'}),
            'empleo_anterior_fin': forms.DateInput(format=('%d/%m/%Y'), attrs={'placeholder': 'Select a date', 'type': 'date'}),
            'empleo_anterior2_inicio': forms.DateInput(format=('%d/%m/%Y'), attrs={'placeholder': 'Select a date', 'type': 'date'}),
            'empleo_anterior2_fin': forms.DateInput(format=('%d/%m/%Y'), attrs={'placeholder': 'Select a date', 'type': 'date'}),
        }


class ofertasEmpleoForm(forms.ModelForm):
    class Meta:
        model = OfertaDeEmpleo
        fields = [
            'titulo',
            'tipo',
            'salario_maximo',
            'salario_minimo',
            'experiencia',
            'categoria',
            'genero',
            'empresa',
            'descripcion',
            'reclutador'
        ]


class EmpresasForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre',
            'logo',
            'direccion',
            'telefono',
            'descripcion',
            'categoria_principal'
        ]


class EditaPerfil(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = [
            "username", "first_name", "last_name",
            "email"
        ]


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)


class CategoriasTrabajoForm(forms.ModelForm):
    class Meta:
        model = OfertaDeEmpleo
        fields = ['categoria']
