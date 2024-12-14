from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth import get_user_model

from .models.usuario import Usuario  
from .models.ejemplar import Ejemplar     
from .models.boleta import Boleta
from .models.categoria import Categoria   
from .models.historial import Historial   
from .models.prestamos import Prestamos   
from .models.tema import Tema   
from .models.venta import Venta   
from .models.autor import Autor         
from .models.carrito import Carrito

User = get_user_model()

def get_current_user():
    from threading import local
    current_user = local()
    return getattr(current_user, 'user', None)

def update_modified_and_user(instance):
    instance.modified = timezone.now()
    user = get_current_user()
    if instance.pk and user:
        instance.user_modified = user

def set_created_user(instance, created):
    user = get_current_user()
    if created and user:
        if not instance.user_created:
            instance.user_created = user
        instance.save()

@receiver(pre_save, sender=Usuario)
def usuario_pre_save(sender, instance, **kwargs):
    update_modified_and_user(instance)

@receiver(post_save, sender=Usuario)
def usuario_post_save(sender, instance, created, **kwargs):
    set_created_user(instance, created)

@receiver(pre_save, sender=Ejemplar)
def ejemplar_pre_save(sender, instance, **kwargs):
    update_modified_and_user(instance)

@receiver(post_save, sender=Ejemplar)
def ejemplar_post_save(sender, instance, created, **kwargs):
    set_created_user(instance, created)

@receiver(pre_save, sender=Boleta)
def boleta_pre_save(sender, instance, **kwargs):
    update_modified_and_user(instance)

@receiver(post_save, sender=Boleta)
def boleta_post_save(sender, instance, created, **kwargs):
    set_created_user(instance, created)

@receiver(pre_save, sender=Categoria)
def categoria_pre_save(sender, instance, **kwargs):
    update_modified_and_user(instance)

@receiver(post_save, sender=Categoria)
def categoria_post_save(sender, instance, created, **kwargs):
    set_created_user(instance, created)

@receiver(pre_save, sender=Historial)
def historial_pre_save(sender, instance, **kwargs):
    update_modified_and_user(instance)

@receiver(post_save, sender=Historial)
def historial_post_save(sender, instance, created, **kwargs):
    set_created_user(instance, created)

@receiver(pre_save, sender=Prestamos)
def prestamos_pre_save(sender, instance, **kwargs):
    update_modified_and_user(instance)

@receiver(post_save, sender=Prestamos)
def prestamos_post_save(sender, instance, created, **kwargs):
    set_created_user(instance, created)

@receiver(pre_save, sender=Tema)
def tema_pre_save(sender, instance, **kwargs):
    update_modified_and_user(instance)

@receiver(post_save, sender=Tema)
def tema_post_save(sender, instance, created, **kwargs):
    set_created_user(instance, created)

@receiver(pre_save, sender=Venta)
def venta_pre_save(sender, instance, **kwargs):
    update_modified_and_user(instance)

@receiver(post_save, sender=Venta)
def venta_post_save(sender, instance, created, **kwargs):
    set_created_user(instance, created)

@receiver(pre_save, sender=Autor)
def autor_pre_save(sender, instance, **kwargs):
    update_modified_and_user(instance)

@receiver(post_save, sender=Autor)
def autor_post_save(sender, instance, created, **kwargs):
    set_created_user(instance, created)

@receiver(pre_save, sender=Carrito)
def carrito_pre_save(sender, instance, **kwargs):
    update_modified_and_user(instance)

@receiver(post_save, sender=Carrito)
def carrito_post_save(sender, instance, created, **kwargs):
    set_created_user(instance, created)