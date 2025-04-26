from django.db import models
from autoslug.fields import AutoSlugField

# Create your models here.

class Category(models.Model):
    name = models.CharField(default="False", max_length=100, null=False)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        # db_table='Categorias'
        verbose_name="Categoria"
        verbose_name_plural="Categorias"