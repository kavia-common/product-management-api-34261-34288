from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model with basic non-negative validations.
    """

    # Explicitly define to ensure validation messages are clear
    price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    quantity = serializers.IntegerField(min_value=0)

    class Meta:
        model = Product
        fields = ["id", "name", "price", "quantity", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
