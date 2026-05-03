from django.db import models
from autoslug import AutoSlugField
from categorias.models import Categoria

# Create your models here.
class Receta(models.Model):
    categorias = models.ForeignKey(Categoria, models.DO_NOTHING) # , default=1
    nombre = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(populate_from= 'nombre', max_length=100)
    tiempo =models.CharField(max_length=100,null=True)
    foto =models.CharField(max_length=100,null=True)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre

    class Meta:
        db_table= 'recetas'
        verbose_name= 'Receta'
        verbose_name_plural = 'Recetas'