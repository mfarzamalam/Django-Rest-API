from django.urls import path, include
from staff.api.views import UserApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('UserApi', UserApi, basename='UserApi')

urlpatterns = [
    path('',include(router.urls)),
]