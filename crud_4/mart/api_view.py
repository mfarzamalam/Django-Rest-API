from typing import List
from django.core.exceptions import ValidationError
from django.http import response
from rest_framework import pagination, serializers
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .serialize import ProductSerializer
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination


class ProductPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 100

class AllProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends  = (DjangoFilterBackend, SearchFilter)
    filter_fields    = ('id',)
    search_fields    = ('name', 'description')
    pagination_class = ProductPagination


    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale is None:
            return super().get_queryset()

        queryset = Product.objects.all()
        if on_sale.lower() == "true":
            queryset.filter(on_sale=True)


        return queryset



class CreateProduct(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price':'Price must be greater than zero'})
        except ValueError:
            raise ValidationError({'price':'A valid number is required'})

        return super().create(request, *args, **kwargs)



class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)

        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(id))

        return response

    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)

        if response.status_code == 200:
            from django.core.cache import cache
            product = response.data
            cache.set('product_data_{}'.format(product['id']),{
                'name':product['name'],
                'description':product['description'],
                'price':product['price'],
            })

        return response