from django.urls import path, include
from .views import StudentApi
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('studentApi', StudentApi, basename='studentapi')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
]