from django.urls import path
from .views import StudentApi, check

urlpatterns = [
    path('student/', StudentApi.as_view()),
    path('check/', check),
]