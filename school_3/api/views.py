from django.shortcuts import render
from .serializers import StudentSerializer
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def post(self, request, *args, **kwargs):
        json_data  = request.body
        bytes_data = io.BytesIO(json_data)
        python_data= JSONParser().parse(bytes_data)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data Created Successfully'}
            json_data= JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data= JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')