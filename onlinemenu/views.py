from rest_framework import viewsets
from .models import Restaurant, Product
from .serializers import RestaurantSerializer, ProductSerializer, RestaurantDetailSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RestaurantDetailSerializer
        return RestaurantSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'retrieve':
            queryset = queryset.prefetch_related(
                'categories',
                'categories__products'
            )
        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_active=True)


# seed data
# delete db, delete migration, makemigration, migrate, superuser, restuarn, prodct, 


# management/commands/seed_data.py