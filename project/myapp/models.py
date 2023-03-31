from django.db import models

# Create your models here.
class Producto(models.Model):
    slug = models.SlugField(unique=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre