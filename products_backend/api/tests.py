from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Product
from decimal import Decimal

class HealthTests(APITestCase):
    def test_health(self):
        url = reverse('Health')  # Make sure the URL is named
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Server is up!"})


class ProductsTotalBalanceTests(APITestCase):
    def test_total_balance_empty(self):
        url = reverse('products-total-balance')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"total_balance": "0.00"})

    def test_total_balance_with_data(self):
        # Create sample products
        Product.objects.create(name="Item A", price=Decimal("10.00"), quantity=2)   # 20.00
        Product.objects.create(name="Item B", price=Decimal("5.50"), quantity=3)    # 16.50
        Product.objects.create(name="Item C", price=Decimal("0.00"), quantity=100)  # 0.00

        url = reverse('products-total-balance')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # 20.00 + 16.50 = 36.50
        self.assertEqual(response.data, {"total_balance": "36.50"})
