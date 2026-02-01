from rest_framework import serializers
from .models import Product
from apps.categories.serializer import CategoryDetailSerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategoryDetailSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'product_stock',
            'category',
            'created_at',
            'updated_at',
            ] 
        read_only_fields = ['id', 'created_at', 'updated_at']
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'product_stock',
            'category_id',
        ]
class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'product_stock',
            'category_id',
            'is_active',
        ]
class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategoryDetailSerializer(read_only=True,many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'product_stock',
            'category',
            'created_at',
            'updated_at',
            'is_active',
        ]