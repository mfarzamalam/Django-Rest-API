from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['GET', 'POST'])
def hello_api(request):
    if request.method == "GET":
        return Response({'msg':'This is from GET'})

    if request.method == "POST":
        return Response({'msg':'This is from POST'})