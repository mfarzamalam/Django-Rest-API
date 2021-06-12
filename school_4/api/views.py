from django.shortcuts import render
from django.views import View
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentModelSerializer
from .models      import Student

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def post(self, request, *args, **kwargs):
        seats = Student.objects.all()
        total = seats.count()
        print(total)
        json_data   = request.body
        bytes_data  = io.BytesIO(json_data)
        python_data = JSONParser().parse(bytes_data)
        serializer  = StudentModelSerializer(data=python_data)

        if serializer.is_valid():
            try:
                serializer.save()
                response  = {'msg':'Data Created Successfully'}
            except:
                response  = {'msg':'Some fields are restricted. you cannot insert more data'}

            json_response = JSONRenderer().render(response)
            return HttpResponse(json_response, content_type='application/json')
        else:
            json_response = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_response, content_type='application/json')


    def get(self, request, *args, **kwargs):
        json_data    = request.body
        bytes_data   = io.BytesIO(json_data)
        python_data  = JSONParser().parse(bytes_data)
        id           = python_data.get('id', None)

        if id is not None:
            student  = Student.objects.get(id=id)
            serializer = StudentModelSerializer(student)
            json_response = JSONRenderer().render(serializer.data)
            return HttpResponse(json_response, content_type='application/json')
        else:
            student  = Student.objects.all()
            serializer = StudentModelSerializer(student, many=True)
            json_response = JSONRenderer().render(serializer.data)
            return HttpResponse(json_response, content_type='application/json')