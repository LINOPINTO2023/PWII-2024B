from django.urls import path, include, re_path
from rest_framework import routers
from libon import views

router = routers.DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'boletas', views.BoletaViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'ejemplares', views.EjemplarViewSet)
router.register(r'historiales', views.HistorialViewSet)
router.register(r'prestamos', views.PrestamosViewSet)
router.register(r'temas', views.TemaViewSet)
router.register(r'ventas', views.VentaViewSet)
router.register(r'carritos', views.CarritoViewSet)

urlpatterns = [
    path('usuarios/', views.UsuarioCreate.as_view(), name='crear-usuario'),
    path('usuarios/lista/', views.UsuarioList.as_view(), name='listar-usuarios'),
    path('usuarios/<int:pk>/', views.UsuarioUpdateDeleteView.as_view(), name='usuario-update-delete'),
    path('', include(router.urls)),
    re_path('login/',views.login, name='api-login'),
]
