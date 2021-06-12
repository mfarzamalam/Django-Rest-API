from django.urls import path
from .views import StudentApi

urlpatterns = [
    path('', StudentApi)
]
