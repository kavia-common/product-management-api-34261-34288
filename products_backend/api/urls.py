from django.urls import path
from .views import health, products_list_create, product_detail

urlpatterns = [
    path('health/', health, name='Health'),
    path('products/', products_list_create, name='products-list-create'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
]
