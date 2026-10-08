from django import forms
from .models import Instrumento

class InstrumentoForm(forms.ModelForm):
    """Formulario para Crear Instrumento"""
    class Meta:
        model = Instrumento
        fields = ['nombre', 'marca', 'categoria', 'precio', 'stock', 'anio_fabricacion', 'imagen_url', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Guitarra Eléctrica Stratocaster'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Fender'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 750000'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 10'}),
            'anio_fabricacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 2023'}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class InstrumentoEditarForm(forms.ModelForm):
    """Formulario para Modificar Instrumento (Distinto diseño/atributos si se requiere)"""
    class Meta:
        model = Instrumento
        fields = ['nombre', 'marca', 'categoria', 'precio', 'stock', 'anio_fabricacion', 'imagen_url', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'marca': forms.TextInput(attrs={'class': 'form-control bg-light'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'anio_fabricacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }