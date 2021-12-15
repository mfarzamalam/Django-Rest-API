from django.db.models import fields
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','price','description')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['on_sale'] = False
        data['current_price'] = instance.price

        return data