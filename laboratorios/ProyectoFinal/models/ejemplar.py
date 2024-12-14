from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid

from django.conf import settings
from django.utils import timezone
from .autor import Autor
from .categoria import Categoria
from .tema import Tema

class Ejemplar(models.Model):
    titulo = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='ejemplares', default='imagen_default.png', verbose_name='imagen')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="ejemplares")
    tema = models.ManyToManyField(Tema , related_name="ejemplares")
    año = models.CharField(max_length=50)
    autor = models.ManyToManyField(Autor, related_name="ejemplares")
    sinopsis = models.TextField(null=True, blank=True)
    paginas = models.IntegerField()
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ejemplares_created', on_delete=models.SET_NULL, null=True, editable=False)
    user_modified = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ejemplares_modified', on_delete=models.SET_NULL, null=True, editable=False)

    def __str__(self):
        return self.titulo