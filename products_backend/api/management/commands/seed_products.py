from django.core.management.base import BaseCommand
from api.models import Product


class Command(BaseCommand):
    help = "Seed the database with a few sample products."

    def handle(self, *args, **options):
        samples = [
            {"name": "Notebook", "price": 3.99, "quantity": 150},
            {"name": "Wireless Mouse", "price": 19.99, "quantity": 75},
            {"name": "USB-C Cable", "price": 7.49, "quantity": 200},
        ]

        created = 0
        for item in samples:
            obj, was_created = Product.objects.get_or_create(
                name=item["name"],
                defaults={
                    "price": item["price"],
                    "quantity": item["quantity"],
                },
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Seed complete. Created {created} new products."))
