from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from onlinemenu.models import Restaurant, ProductCategory, Product




User = get_user_model()


class Command(BaseCommand):
    help = "Seed database with initial restaurant data"

    def handle(self, *args, **options):
        # Get or create a default user to own the restaurants
        user, created = User.objects.get_or_create(
            username="admin",
            defaults={"fullname": "Seed User", "phone": "0900000000"},
        )
        if created:
            user.set_password("admin")
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created user: {user.username}"))

        # Restaurant data
        restaurants_data = [
            {"name": "mora", "label": "Mora Restaurant", "phone": "021-11111111"},
            {"name": "gilahij", "label": "Gilahij Restaurant", "phone": "021-22222222"},
        ]

        # Categories for each restaurant
        categories_data = ["food", "drink", "fast-food", "coffee"]

        # Products for each category
        products_data = {
            "food": [
                {"name": "Grilled Chicken", "label": "Juicy grilled chicken breast", "price": 150000},
                {"name": "Beef Steak", "label": "Tender beef steak with sauce", "price": 250000},
                {"name": "Seafood Pasta", "label": "Pasta with fresh seafood", "price": 180000},
            ],
            "drink": [
                {"name": "Fresh Orange Juice", "label": "Freshly squeezed orange juice", "price": 40000},
                {"name": "Mineral Water", "label": "Natural mineral water 500ml", "price": 15000},
                {"name": "Iced Tea", "label": "Refreshing iced tea with lemon", "price": 35000},
            ],
            "fast-food": [
                {"name": "Cheeseburger", "label": "Classic cheeseburger with fries", "price": 120000},
                {"name": "Chicken Nuggets", "label": "Crispy chicken nuggets (8 pcs)", "price": 90000},
                {"name": "Hot Dog", "label": "Beef hot dog with toppings", "price": 80000},
            ],
            "coffee": [
                {"name": "Espresso", "label": "Strong Italian espresso", "price": 30000},
                {"name": "Cappuccino", "label": "Espresso with steamed milk foam", "price": 45000},
                {"name": "Latte", "label": "Espresso with steamed milk", "price": 50000},
            ],
        }

        for rest_data in restaurants_data:
            restaurant, created = Restaurant.objects.get_or_create(
                name=rest_data["name"],
                defaults={
                    "owner": user,
                    "label": rest_data["label"],
                    "phone": rest_data["phone"],
                    "rank": 5,
                    "is_active": True,
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created restaurant: {restaurant.name}"))
            else:
                self.stdout.write(f"Restaurant already exists: {restaurant.name}")

            for cat_name in categories_data:
                category, created = ProductCategory.objects.get_or_create(
                    restaurant=restaurant,
                    name=cat_name,
                    defaults={
                        "label": cat_name.title(),
                        "is_active": True,
                    },
                )
                if created:
                    self.stdout.write(f"  Created category: {category.name}")

                for prod_data in products_data[cat_name]:
                    product, created = Product.objects.get_or_create(
                        category=category,
                        name=prod_data["name"],
                        defaults={
                            "label": prod_data["label"],
                            "price": prod_data["price"],
                            "rank": 5,
                            "is_active": True,
                        },
                    )
                    if created:
                        self.stdout.write(f"    Created product: {product.name} ({product.price})")

        self.stdout.write(self.style.SUCCESS("Seeding completed successfully!"))