from django.shortcuts import render
from .models import School
from .serializers import SchoolSerializer
from rest_framework.viewsets import ModelViewSet
from .paginations import CustomPagination, CustomLimitOffset


# Create your views here.
# class SchoolApi(ModelViewSet):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
#     pagination_class = CustomPagination



class SchoolApi(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class = CustomLimitOffset