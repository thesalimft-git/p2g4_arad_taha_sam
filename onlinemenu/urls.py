from .views import RestaurantViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurants')
router.register(r'products', ProductViewSet, basename='products')
urlpatterns = router.urls


# resturant/1/categories/3/prodcuts/1/


# restaurants/2/ + categories + first category products
# restaurants/2/categories/
# restaurants/2/categories/1/products/