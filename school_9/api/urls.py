from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentApi4


router = DefaultRouter()
router.register('studentapi', StudentApi4, basename='studentapi')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls')),
]
