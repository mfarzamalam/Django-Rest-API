from django.urls import path
# from .views import hello_api
from .views import student_api

urlpatterns = [
    path('studentApi/', student_api),
    path('studentApi/<int:pk>/', student_api),
]
