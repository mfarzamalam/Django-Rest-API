from django.urls import path


from mart.api_view import AllProductList, CreateProduct, ProductRetrieveUpdateDestroy

urlpatterns = [
    path('api/v1/products/', AllProductList.as_view()),
    path('api/v1/products/new', CreateProduct.as_view()),
    path('api/v1/products/<int:id>/', ProductRetrieveUpdateDestroy.as_view()),
]
