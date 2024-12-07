from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComicViewSet, HistorialViewSet

# Enrutador DRF
router = DefaultRouter()
router.register(r'comics', ComicViewSet)
router.register(r'historial', HistorialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
