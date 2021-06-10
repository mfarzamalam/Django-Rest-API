from django.shortcuts import render
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from django.http import HttpResponse

# Create your views here.
def student_get(request):
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