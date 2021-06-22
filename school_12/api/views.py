from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentApi(ListAPIView):    
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.filter(faculty_name=self.request.user)