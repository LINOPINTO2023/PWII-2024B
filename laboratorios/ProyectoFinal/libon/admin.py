from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.usuario import Usuario
from .models.boleta import Boleta
from .models.historial import Historial
from .models.autor import Autor
from .models.tema import Tema
from .models.categoria import Categoria
from .models.ejemplar import Ejemplar
from .models.venta import Venta
from .models.prestamos import Prestamos
from .models.carrito import Carrito

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('dni', 'direccion', 'telefono')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'dni', 'direccion', 'telefono')}),
    )
admin.site.register(Usuario, UsuarioAdmin)

def get_current_user(request):
    return request.user if request.user.is_authenticated else None

class CustomAdmin(admin.ModelAdmin):
    exclude = ('created', 'modified', 'user_created', 'user_modified')

    def save_model(self, request, obj, form, change):
        user = get_current_user(request)
        if not obj.pk:
            obj.user_created = user
        obj.user_modified = user
        super().save_model(request, obj, form, change)

admin.site.register(Boleta, CustomAdmin)
admin.site.register(Historial, CustomAdmin)
admin.site.register(Autor, CustomAdmin)
admin.site.register(Tema, CustomAdmin)
admin.site.register(Categoria, CustomAdmin)
admin.site.register(Ejemplar, CustomAdmin)
admin.site.register(Venta, CustomAdmin)
admin.site.register(Prestamos, CustomAdmin)
admin.site.register(Carrito, CustomAdmin)