from django.urls import path, include
from .views import SchoolApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('schoolApi', SchoolApi, basename='schoolApi')

urlpatterns = [
    path('',include(router.urls)),
]