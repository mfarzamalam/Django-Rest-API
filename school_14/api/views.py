from django.shortcuts import render
from .serializers import SingerSerializer, SongSerializer, StudentSerializer
from rest_framework import viewsets
from .models import Song, Singer, Student


# Create your views here.
class SongApi(viewsets.ModelViewSet):
    queryset  = Song.objects.all()
    serializer_class = SongSerializer


class SingerApi(viewsets.ModelViewSet):
    queryset  = Singer.objects.all()
    serializer_class = SingerSerializer


class StudentApi(viewsets.ModelViewSet):
    queryset  = Student.objects.all()
    serializer_class = StudentSerializer