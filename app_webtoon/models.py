from django.db import models
from django.utils import timezone
# Create your models here.

class Webtoon(models.Model):
    # Opciones para el campo "género"
    GENEROS = [
        ('ACCION', 'Acción'),
        ('AVENTURA', 'Aventura'),
        ('COMEDIA', 'Comedia'),
        ('DRAMA', 'Drama'),
        ('FANTASIA', 'Fantasía'),
        ('ROMANCE', 'Romance'),
        ('TERROR', 'Terror'),
        ('MISTERIO', 'Misterio'),
        ('OTRO', 'Otro'),
    ]

    # Opciones para el campo "estado"
    ESTADOS = [
        ('EN_CURSO', 'En curso'),
        ('FINALIZADO', 'Finalizado'),
        ('PAUSADO', 'Pausado'),
    ]

    id_webtoon = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, unique=True)
    id_creador = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField()
    genero = models.CharField(max_length=50, choices=GENEROS, default='OTRO')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='EN_CURSO')
    fecha_publicacion = models.DateField(default=timezone.now)
    portada_url = models.URLField(max_length=255)
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Webtoon: {self.titulo} - {self.genero} - Estado: {self.estado}'
