from rest_framework import viewsets

from productMsApp.models.product import Product
from productMsApp.serializers.productSerializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
