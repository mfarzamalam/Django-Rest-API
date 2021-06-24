from django.shortcuts import render
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets
from .models import Song, Singer


# Create your views here.
class SongApi(viewsets.ModelViewSet):
    queryset  = Song.objects.all()
    serializer_class = SongSerializer


class SingerApi(viewsets.ModelViewSet):
    queryset  = Singer.objects.all()
    serializer_class = SingerSerializer