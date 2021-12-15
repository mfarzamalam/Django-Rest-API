from django.db.models import fields
from rest_framework import serializers
from .models import Product, ShoppingCartItem




class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')


class ProductSerializer(serializers.ModelSerializer):
    on_sale = serializers.BooleanField(read_only=True, default=False)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=10, max_length=100)
    cart_items  = serializers.SerializerMethodField()
    # price       = serializers.FloatField(min_value=1.00, max_value=400.00)
    price       = serializers.DecimalField(min_value=1.00, max_value=400.00, decimal_places=2, max_digits=None)
    
    class Meta:
        model = Product
        fields = ('id','name','price','description', 'on_sale', 'current_price', 'cart_items')


    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        return CartItemSerializer(items, many=True).data