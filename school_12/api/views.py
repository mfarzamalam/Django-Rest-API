from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework.backends import DjangoFilterBackend

# Create your views here.
# class StudentApi(ListAPIView):    
#     serializer_class = StudentSerializer
#     def get_queryset(self):
#         return Student.objects.filter(faculty_name=self.request.user)


class StudentApi(ListAPIView): 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends  = [DjangoFilterBackend]
    filterset_fields = ['city', 'faculty_name']