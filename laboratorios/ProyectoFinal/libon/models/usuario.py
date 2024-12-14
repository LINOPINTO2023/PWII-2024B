from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Usuario(AbstractUser):
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=40)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username