from rest_framework import viewsets
from .models import Comic, Historial
from .serializers import ComicSerializer, HistorialSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Bienvenido a HeroesApp</h1>
        <p>Usa las rutas de la API para interactuar con los recursos:</p>
        <ul>
            <li><a href="/api/comics/">Comics</a>: Lista de cómics</li>
            <li><a href="/api/historial/">Historial</a>: Historial de usuarios</li>
        </ul>
    """)


# ViewSet para Comics
class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer

# ViewSet para Historial
class HistorialViewSet(viewsets.ModelViewSet):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer
