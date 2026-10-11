from django.contrib import admin

from .models import (
    Restaurant, 
    Product, 
    ProductCategory, 
    Order, 
    OrderItem
)

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']
    
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Order)
admin.site.register(OrderItem)