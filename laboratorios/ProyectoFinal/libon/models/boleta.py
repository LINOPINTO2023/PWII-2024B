from django.db import models

from django.conf import settings
from django.utils import timezone
from .venta import Venta
from .prestamos import Prestamos

class Boleta(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Cliente')
    ventas = models.ManyToManyField(Venta, limit_choices_to={'status': True},null=True, blank=True)
    prestamos = models.ManyToManyField(Prestamos, limit_choices_to={'status': True},null=True, blank=True)
    pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='boletas_created', on_delete=models.SET_NULL, null=True, editable=False)
    user_modified = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='boletas_modified', on_delete=models.SET_NULL, null=True, editable=False)

    def __str__(self):
        return f"Boleta: { self.cliente.username } - Total: { self.pago }"