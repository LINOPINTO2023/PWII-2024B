from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid

from django.conf import settings
from django.utils import timezone

class Tema(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tema_created', on_delete=models.SET_NULL, null=True, editable=False)
    user_modified = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tema_modified', on_delete=models.SET_NULL, null=True, editable=False)

    def __str__(self):
        return self.nombre