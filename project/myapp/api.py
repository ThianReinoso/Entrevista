from .models import Producto
from rest_framework import viewsets, permissions, pagination
from .serializer import ProductSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer