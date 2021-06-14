from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView

# Create your views here.

class student_api(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'msg':'Data created successfully'})
            except:
                return Response({'msg':'You cannot add more data.'})
        else:
            return Response(serializer.errors)

    
    def put(self, request, pk, format=None):
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        else:
            return Response(serializer.errors)


    def patch(self, request, pk, format=None):
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        else:
            return Response(serializer.errors)


    def delete(self, request, pk, format=None):
        id = pk
        try:
            student = Student.objects.get(pk=id)
            student.delete()
            return Response({'msg':'Data is deleted'})
        except:
            return Response({'msg':'Error in deleting data'})