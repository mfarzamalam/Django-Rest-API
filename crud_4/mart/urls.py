from django.urls import path
from mart.api_view import AllProductList

urlpatterns = [
    path('api/v1/products/', AllProductList.as_view()),
]
