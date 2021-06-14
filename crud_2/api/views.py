from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.


# @api_view() ### Get is by default ###
# def hello_api(request):
#     return Response({'msg':'Hello to the new world'})


# @api_view(['POST'])
# def hello_api(request):
#     print(request.data)
#     return Response({'msg':'This is from post data'})


# @api_view(['GET', 'POST'])
# def hello_api(request):
#     return Response({'msg':'This is from post and get'})


# @api_view(['GET', 'POST'])
# def hello_api(request):
#     if request.method == "GET":
#         return Response({'msg':'This is from GET'})

#     if request.method == "POST":
#         return Response({'msg':'This is from POST'})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == "GET":
        id = request.data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)

        return Response(serializer.data)

    
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'msg':'Data created successfully'})
            except:
                return Response({'msg':'You cannot add more data.'})
        else:
            return Response(serializer.errors)


    if request.method == "PUT":
        id = request.data.get('id')
        name = request.data.get('name')
        roll = request.data.get('roll')
        city = request.data.get('city')
        
        student = Student.objects.get(pk=id)

        if name == None or roll == None or city == None:
            serializer = StudentSerializer(student, data=request.data, partial=True)
        else:
            serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data Updated'}
            return Response(response)
        else:
            return Response(serializer.errors)

    
    if request.method == "DELETE":
        id = request.data.get('id')
        try:
            student = Student.objects.get(pk=id)
            student.delete()
            response = {'msg':'Data is deleted'}
            return Response(response)
        except:
            response = {'msg':'Error in deleting data'}
            return Response(response)