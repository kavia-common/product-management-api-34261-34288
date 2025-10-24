from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def health(request):
    """
    Simple health check endpoint.

    Returns:
        200 OK with a JSON message indicating server status.
    """
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
@api_view(['GET', 'POST'])
def products_list_create(request):
    """
    List all products or create a new product.

    GET:
        Summary: List Products
        Description: Returns a list of all products.
        Responses:
            200: JSON array of products.

    POST:
        Summary: Create Product
        Description: Creates a new product with provided name, price, and quantity.
        Request Body (application/json):
            - name: string (required)
            - price: decimal >= 0 (required)
            - quantity: integer >= 0 (required)
        Responses:
            201: Created product JSON.
            400: Validation errors.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PUBLIC_INTERFACE
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk: int):
    """
    Retrieve, update, or delete a product by ID.

    Path Parameters:
        - pk: integer ID of the product

    GET:
        Summary: Retrieve Product
        Description: Get a single product by ID.
        Responses:
            200: Product JSON.
            404: Not found.

    PUT:
        Summary: Update Product
        Description: Replace product fields with provided data.
        Request Body (application/json):
            - name: string (required)
            - price: decimal >= 0 (required)
            - quantity: integer >= 0 (required)
        Responses:
            200: Updated product JSON.
            400: Validation errors.
            404: Not found.

    DELETE:
        Summary: Delete Product
        Description: Deletes the specified product.
        Responses:
            204: No content on successful deletion.
            404: Not found.
    """
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
