from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.


def student_api(request):
    pass