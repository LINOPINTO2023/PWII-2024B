from django.contrib import admin
from .models import Comic, Historial

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('author',)

@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'comic', 'timestamp')
    search_fields = ('user__username', 'comic__title')
    list_filter = ('timestamp',)
