from django.urls import path, include
from .views import StudentApi, StudentApi2
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


router = DefaultRouter()
# router.register('studentApi', StudentApi, basename='studentapi')
router.register('studentApi', StudentApi2, basename='studentapi')


urlpatterns = [
    path('',include(router.urls)),
    # path('gettoken/',TokenObtainPairView.as_view()),
    # path('refreshtoken/',TokenRefreshView.as_view()),
    # path('verifytoken/',TokenVerifyView.as_view()),
    path('auth/',include('rest_framework.urls')),
]