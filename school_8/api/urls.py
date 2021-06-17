from django.urls import path, include
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter


        # Created router object
router = DefaultRouter()

        # Register view with router
router.register('Studentapi', StudentViewSet, basename='student')

urlpatterns = [
    path('',include(router.urls)),
]