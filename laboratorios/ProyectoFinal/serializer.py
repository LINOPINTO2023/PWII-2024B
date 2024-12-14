from rest_framework import serializers
from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import autor, boleta, categoria, ejemplar, historial, prestamos, tema, venta, carrito

User = get_user_model()

class EjemplarFilter(filters.FilterSet):
    categoria = filters.NumberFilter(field_name='categoria', lookup_expr='exact')
    titulo = filters.CharFilter(method='filter_by_search', lookup_expr='icontains')
    
    def filter_by_search(self, queryset, value):
        return queryset.filter(titulo__icontains=value) | queryset.filter(sinopsis__icontains=value) | queryset.filter(nombre_autor__icontains=value)

    class Meta:
        model = ejemplar.Ejemplar
        fields = {
            'categoria': ['exact'],
            'titulo': ['icontains'],
        }

class UsuarioSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'dni', 'direccion', 'telefono', 'is_staff', 'status', 'token')
        extra_kwargs = {
            'password': {'write_only': True}, 
            'token': {'read_only': True}, 
            'email': {'required': True},
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            dni=validated_data.get('dni', ''),
            direccion=validated_data.get('direccion', ''),
            telefono=validated_data.get('telefono', ''),
            is_staff=validated_data.get('is_staff', False),
            status=validated_data.get('status', True)
        )
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.dni = validated_data.get('dni', instance.dni)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()

    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = autor.Autor
        fields = '__all__'

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = boleta.Boleta
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria.Categoria
        fields = '__all__'

class EjemplarSerializer(serializers.ModelSerializer):
    nombre_autor = serializers.SerializerMethodField()
    nombre_categoria = serializers.ReadOnlyField(source='categoria.nombre')
    nombre_tema = serializers.SerializerMethodField()
    class Meta:
        model = ejemplar.Ejemplar
        fields = ('id', 'titulo', 'imagen', 'año', 'sinopsis', 'paginas', 'stock', 'precio', 'status', 'categoria', 'nombre_categoria', 'tema', 'autor', 'nombre_autor', 'nombre_tema')
        filterset_class = EjemplarFilter

    def get_nombre_autor(self, obj):
        autores = obj.autor.all()
        return [autor.nombre for autor in autores]
    
    def get_nombre_tema(self, obj):
        temas = obj.tema.all()
        return [tema.nombre for tema in temas]

class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = historial.Historial
        fields = '__all__'

class PrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = prestamos.Prestamos
        fields = '__all__'

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tema.Tema
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta.Venta
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    ejemplar = EjemplarSerializer(many=True, read_only=True)

    class Meta:
        model = carrito.Carrito
        fields = ('id', 'usuario', 'ejemplar', 'status', 'created', 'modified', 'user_created', 'user_modified')

    def create(self, validated_data):
        ejemplares = validated_data.pop('ejemplar', [])
        carrito = super().create(validated_data)
        carrito.ejemplar.set(ejemplares)
        return carrito
    
    def update(self, instance, validated_data):
        ejemplares = validated_data.pop('ejemplar', [])
        instance = super().update(instance, validated_data)
        instance.ejemplar.set(ejemplares)
        return instance