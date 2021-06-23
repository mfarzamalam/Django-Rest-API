from django.shortcuts import render
from .models import School
from .serializers import SchoolSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class SchoolApi(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer