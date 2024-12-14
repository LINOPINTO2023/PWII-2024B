from django.db import models

from django.conf import settings
from django.utils import timezone
from .boleta import Boleta
from .ejemplar import Ejemplar

class Historial(models.Model):
    cliente = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='historial')
    deudor = models.BooleanField(default=False)
    ejemplares = models.ManyToManyField(Ejemplar, null=True, blank=True)
    boletas = models.ManyToManyField(Boleta, null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='historial_created', on_delete=models.SET_NULL, null=True, editable=False)
    user_modified = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='historial_modified', on_delete=models.SET_NULL, null=True, editable=False)