from django.shortcuts import render
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data  = request.body
        bytes_data     = io.BytesIO(json_data)
        python_data= JSONParser().parse(bytes_data)
        id         = python_data.get('id', None)

        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            json_data  = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            json_data  = JSONRenderer().render(serializer.data)

            return HttpResponse(json_data, content_type='application/json')


    if request.method == "POST":
        json_data  = request.body
        bytes_data = io.BytesIO(json_data)
        python_data= JSONParser().parse(bytes_data)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':'The data is Created'}
            json_data= JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data= JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')


    if request.method == "PUT":
        json_data  = request.body
        bytes_data = io.BytesIO(json_data)
        python_data= JSONParser().parse(bytes_data)
        id         = python_data.get('id')
        name       = python_data.get('name', None)
        city       = python_data.get('city', None)
        desc       = python_data.get('desc', None)
        
        student    = Student.objects.get(id=id)

        if name == None or city == None or desc == None:
            serializer = StudentSerializer(student, data=python_data, partial=True)
        else:
            serializer = StudentSerializer(student, data=python_data)

        if serializer.is_valid():
            serializer.save()
            response  = {'msg':'The data is Updated'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')