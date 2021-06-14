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


@api_view(['GET', 'POST', 'PUT', 'PATCH' , 'DELETE'])
def student_api(request, pk=None):
    if request.method == "GET":
        id = pk
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
        id = pk
        name = request.data.get('name')
        roll = request.data.get('roll')
        city = request.data.get('city')
        
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Complete Data Updated'}
            return Response(response)
        else:
            return Response(serializer.errors)


    if request.method == "PATCH":
        id = pk
        name = request.data.get('name')
        roll = request.data.get('roll')
        city = request.data.get('city')
        
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Partial Data Updated'}
            return Response(response)
        else:
            return Response(serializer.errors)
    

    if request.method == "DELETE":
        id = pk
        try:
            student = Student.objects.get(pk=id)
            student.delete()
            response = {'msg':'Data is deleted'}
            return Response(response)
        except:
            response = {'msg':'Error in deleting data'}
            return Response(response)