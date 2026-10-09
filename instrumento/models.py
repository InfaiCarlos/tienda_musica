from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Instrumento(models.Model):
    CATEGORIAS = [
        ('Cuerda', 'Cuerda'),
        ('Viento', 'Viento'),
        ('Percusión', 'Percusión'),
        ('Teclado', 'Teclado'),
        ('Electrónico', 'Electrónico'),
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre del Instrumento")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, verbose_name="Categoría")
    precio = models.IntegerField(
        validators=[MinValueValidator(100000, message="El precio debe ser mayor a 100.000")],
        verbose_name="Precio ($)"
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(0, message="El stock no puede ser negativo")],
        verbose_name="Stock disponible"
    )
    anio_fabricacion = models.IntegerField(
        validators=[
            MinValueValidator(1800, message="Año no válido"),
            MaxValueValidator(2026, message="El año no puede ser superior al actual")
        ],
        verbose_name="Año de Fabricación"
    )
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return f"{self.nombre} ({self.marca})"