from rest_framework import serializers

from .models import Product, ProductCategory, ProductVendor


# Model Serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVendor
        fields = '__all__'
