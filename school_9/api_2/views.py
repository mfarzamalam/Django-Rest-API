from django.shortcuts import render
from api.models import Student
from api.serialzers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets
from .customPerms import MyPerms


# Create your views here.
class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPerms]