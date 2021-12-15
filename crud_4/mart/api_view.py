from typing import List
from rest_framework import pagination
from rest_framework.generics import ListAPIView
from .serialize import ProductSerializer
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination


class ProductPagination(LimitOffsetPagination):
    default_limit = 1
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