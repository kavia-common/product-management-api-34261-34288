from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """
    Product model representing items with a name, price, and quantity.

    Fields:
        name (str): Name of the product.
        price (decimal): Non-negative price with 2 decimal places.
        quantity (int): Non-negative quantity available.
        created_at (datetime): Auto-added creation timestamp.
        updated_at (datetime): Auto-updated modification timestamp.
    """
    name = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.name} (${self.price}) x {self.quantity}"
