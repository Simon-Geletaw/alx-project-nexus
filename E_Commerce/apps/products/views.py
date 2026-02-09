from django.shortcuts import render
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import ProductSerializer, ProductCreateSerializer, ProductUpdateSerializer, ProductDetailSerializer
from .models import Product
from apps.categories.serializer import CategoryDetailSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = (permissions.AllowAny,)

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = (permissions.AllowAny,)


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = (permissions.IsAdminUser,)
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = (permissions.IsAdminUser,)