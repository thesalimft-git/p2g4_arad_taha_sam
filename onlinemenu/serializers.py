from .models import Restaurant, Product, ProductCategory
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class RestaurantDetailSerializer(serializers.ModelSerializer):
    categories = ProductCategorySerializer(many=True, read_only=True)
    products = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = '__all__'

    def get_products(self, obj):
        first_category = obj.categories.first()
        if first_category:
            products = first_category.products.filter(is_active=True)
            return ProductSerializer(products, many=True).data
        return []
