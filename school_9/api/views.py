from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serialzers import StudentSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny, 
    IsAdminUser, 
    IsAuthenticatedOrReadOnly, 
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly,
)

# Create your views here.
class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]



class StudentApi2(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]     #Overwrite the default authentication



class StudentApi3(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAdminUser]




class StudentApi4(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAdminUser]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]