from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','PUT','DELETE'])
def chk_api(request):
    if request.method=='GET':
        return Response({'msg':'get request'})

    if request.method=='POST':
        print(request.data)
        return Response({'msg':'post request'})

    if request.method=='PUT':
        print(request.data)
        return Response({'msg':'put request'})

    if request.method=='DELETE':
        return Response({'msg':'delete request'})
