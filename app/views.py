from rest_framework import generics

from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
