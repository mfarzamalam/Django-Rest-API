from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

# For single objects
def StudentJsonObjectView(request):
    students = Student.objects.get(id=1)
    serializer = StudentSerializers(students)
    # json_data  = JSONRenderer().render(serializer.data)

    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data)


# For Querysets
def StudentJsonQuerySetView(request):
    students = Student.objects.all()
    serializer = StudentSerializers(students, many=True)
    json_data  = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type='application/json')