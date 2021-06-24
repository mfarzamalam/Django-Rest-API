from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SingerApi, SongApi, StudentApi


router = DefaultRouter()
router.register('SongApi', SongApi, basename='song')
router.register('SingerApi', SingerApi, basename='singer')
router.register('StudentApi', StudentApi, basename='student')


urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
]