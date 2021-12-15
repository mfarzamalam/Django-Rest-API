from django.urls import path


from mart.api_view import AllProductList, CreateProduct, ProductDestroy

urlpatterns = [
    path('api/v1/products/', AllProductList.as_view()),
    path('api/v1/products/new', CreateProduct.as_view()),
    path('api/v1/products/<int:id>/destroy', ProductDestroy.as_view()),
]
