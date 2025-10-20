from django import forms
from .models import Webtoon

class WebtoonForm(forms.ModelForm):
    class Meta:
        model = Webtoon
        fields = [
            'titulo',
            'genero',
            'descripcion',
            'estado',
            'fecha_publicacion',
            'portada_url',
            'calificacion_promedio'
        ]
        labels = {
            'titulo': 'Título del Webtoon',
            'genero': 'Género',
            'descripcion': 'Descripción',
            'estado': 'Estado',
            'fecha_publicacion': 'Fecha de Publicación',
            'portada_url': 'URL de Portada',
            'calificacion_promedio': 'Calificación Promedio',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'portada_url': forms.URLInput(attrs={'class': 'form-control'}),
            'calificacion_promedio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
