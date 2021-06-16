from django.urls import path
from .views import StudentListCreate, StudentRetrieveUpdateDestroy

urlpatterns = [
    path('StudentApi/', StudentListCreate.as_view()),
    path('StudentApi/<int:pk>/', StudentRetrieveUpdateDestroy.as_view()),
]