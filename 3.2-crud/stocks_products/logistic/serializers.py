from rest_framework import serializers
from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(stock=stock,
                                        product=position['product'],
                                        quantity=position['quantity'],
                                        price=position['price'],
                                        )
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        stocks_products = StockProduct.objects.filter(stock=stock)
        products = [product['product'] for product in positions]

        for product in stocks_products:
            if product.product not in products:
                product.delete()

        for position in positions:
            StockProduct.objects.update_or_create(stock=stock, product=position['product'], defaults={
                    'product': position['product'],
                    'quantity': position['quantity'],
                    'price': position['price']
                })

        return stock
