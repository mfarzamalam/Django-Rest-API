from django.shortcuts import render
from .models import Student
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.
class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        folks = Student.objects.all()
        serializer = StudentSerializer(folks, many=True)

        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        if pk is not None:
            chap = Student.objects.get(pk=pk)
            serializer = StudentSerializer(chap)

            return Response(serializer.data)


    def create(self, request):
        serialzer = StudentSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({"msg":"Created, Sire"})
        else:
            return Response({"msg":"Mayday"})


    def update(self, request, pk=None):
        if pk is not None:
            lad = Student.objects.get(pk=pk)
            serializer = StudentSerializer(lad, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Updated, Sire"})
            else:
                return Response({"msg":"Mayday"})


    def partial_update(self, request, pk=None):
        if pk is not None:
            lad = Student.objects.get(pk=pk)
            serializer = StudentSerializer(lad, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Update Partial, Sire"})
            else:
                return Response({"msg":"Mayday"})


    def destroy(self, request, pk=None):
        if pk is not None:
            bogey = Student.objects.get(pk=pk)
            bogey.delete()
            return Response({"msg":"Tango Down"})



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer