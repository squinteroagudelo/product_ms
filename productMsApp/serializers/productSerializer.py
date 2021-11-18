from rest_framework import serializers
from productMsApp.models.product import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "product_name", "product_stock", "product_price", "is_active"]

    def to_representation(self, obj):
        product = Product.objects.get(id=obj.id)
        return {
            'id': product.id,
            'name': product.product_name,
            'stock': product.product_stock,
            'price': product.product_price,
            'active': product.is_active,
        }
