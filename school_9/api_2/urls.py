from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentApi


router = DefaultRouter()
router.register('studentapi', StudentApi, basename='studentapi')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls')),
]
