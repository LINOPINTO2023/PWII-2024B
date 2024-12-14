from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid

from django.conf import settings
from django.utils import timezone
from .ejemplar import Ejemplar
from .usuario import Usuario

class Venta(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Cliente')
    ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE, verbose_name='Ejemplar')
    cantidad = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='venta_created', on_delete=models.SET_NULL, null=True, editable=False)
    user_modified = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Venta_modified', on_delete=models.SET_NULL, null=True, editable=False)

    def __str__(self):
        return f'Venta: {self.cliente} - {self.ejemplar} - {self.created}'