from django.urls import path, include
from .views import student_get

urlpatterns = [
    path('student/', student_get),

]