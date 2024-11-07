# juego/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.juego_view, name='juego'),
]
