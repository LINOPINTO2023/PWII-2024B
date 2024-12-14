from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid

from django.conf import settings
from django.utils import timezone
from .ejemplar import Ejemplar
from .usuario import Usuario

class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, verbose_name='Cliente')
    ejemplar = models.ManyToManyField(Ejemplar, verbose_name='Ejemplares')
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='carrito_created', on_delete=models.SET_NULL, null=True, editable=False)
    user_modified = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='carrito_modified', on_delete=models.SET_NULL, null=True, editable=False)
