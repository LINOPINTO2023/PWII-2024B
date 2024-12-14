from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializer import *
from .models import usuario, autor, boleta, categoria, historial, prestamos, tema, venta
from .models.ejemplar import Ejemplar
from .models.carrito import Carrito
from .models.usuario import Usuario

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework import status
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate
User = get_user_model()

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, email=request.data['email'])

    if not user.check_password(request.data['password']):
        return Response({"error":"Invalid Password"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UsuarioSerializer(instance=user)
    return Response({"token":token.key, 
                     "user_id": user.id,
                     "user":serializer.data}, 
                     status=status.HTTP_200_OK)

class UsuarioCreate(generics.CreateAPIView):
    queryset = usuario.Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny] 

class UsuarioList(generics.ListAPIView):
    queryset = usuario.Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class UsuarioUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class AutorViewSet(viewsets.ModelViewSet):
    queryset = autor.Autor.objects.all()
    serializer_class = AutorSerializer

class BoletaViewSet(viewsets.ModelViewSet):
    queryset = boleta.Boleta.objects.all()
    serializer_class = BoletaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = categoria.Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]

class EjemplarViewSet(viewsets.ModelViewSet):
    queryset = Ejemplar.objects.all()
    serializer_class = EjemplarSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()

        categoria = self.request.query_params.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria=categoria)

        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(titulo__icontains=search) | queryset.filter(sinopsis__icontains=search) | queryset.filter(autor__nombre__icontains=search)

        return queryset

class HistorialViewSet(viewsets.ModelViewSet):
    queryset = historial.Historial.objects.all()
    serializer_class = HistorialSerializer

class PrestamosViewSet(viewsets.ModelViewSet):
    queryset = prestamos.Prestamos.objects.all()
    serializer_class = PrestamosSerializer
    
class TemaViewSet(viewsets.ModelViewSet):
    queryset = tema.Tema.objects.all()
    serializer_class = TemaSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = venta.Venta.objects.all()
    serializer_class = VentaSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Carrito.objects.filter(usuario=self.request.user)

    def create(self, request, *args, **kwargs):
        usuario = request.user
        carrito, created = Carrito.objects.get_or_create(usuario=usuario)

        ejemplar_ids = request.data.get('ejemplar', [])

        if ejemplar_ids:
            for ejemplar_id in ejemplar_ids:
                ejemplar = get_object_or_404(Ejemplar, id=ejemplar_id)
                carrito.ejemplar.add(ejemplar)
            carrito.save()

        serializer = self.get_serializer(carrito)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        carrito = self.get_object()

        ejemplar_id = request.data.get('ejemplar_id')
        
        if ejemplar_id:
            ejemplar = carrito.ejemplar.filter(id=ejemplar_id).first()
            if ejemplar:
                carrito.ejemplar.remove(ejemplar)
                carrito.save()
                return Response({'status': 'Ejemplar eliminado'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Ejemplar no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        return super().update(request, *args, **kwargs)