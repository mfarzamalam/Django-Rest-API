from django.urls import path, include
from .views import student_api

urlpatterns = [
    path('studentapi/', student_api),
]