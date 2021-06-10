from django.urls import path
from .views import StudentApi

urlpatterns = [
    path('student/', StudentApi.as_view()),
]