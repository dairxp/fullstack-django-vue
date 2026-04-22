from django.db import models

# Create your models here.
class Receta(models, Model):
    nombre = models.CharField(max_length==100, null=False)
    slug = AutoSlugField(populate_from= 'nombre', max_length=100)
    tiempo =models.CharField(maz_length=100,null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table= 'categorias'
        verbose_name= 'Categoria'
        verbose_name_plural = 'Categorias'