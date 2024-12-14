from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid

from django.conf import settings
from django.utils import timezone

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='autores', default='imagen_default.png', verbose_name='imagen')
    nacionalidad = models.CharField(max_length=50)
    biografia = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='autors_created', on_delete=models.SET_NULL, null=True, editable=False)
    user_modified = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='autors_modified', on_delete=models.SET_NULL, null=True, editable=False)

    def __str__(self):
        return self.nombre