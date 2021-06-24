from django.shortcuts import render
from .models import School
from .serializers import SchoolSerializer
from rest_framework.viewsets import ModelViewSet
from .paginations import (
    CustomPageNumberPagination,
    CustomLimitOffsetPagination,
    CustomCursorPagination,
)


# Create your views here.
# class SchoolApi(ModelViewSet):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
#     pagination_class = CustomPageNumberPagination



# class SchoolApi(ModelViewSet):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
#     pagination_class = CustomLimitOffsetPagination



class SchoolApi(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class = CustomCursorPagination