from django.db import models
from autoslug import AutoSlugField

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(populate_from='nombre')

    def __str__(self):
        return self.nombre
    class Meta:
        db_table='categorias'
        verbose_name='Categorias'
        verbose_name_plural='Categorias'
        