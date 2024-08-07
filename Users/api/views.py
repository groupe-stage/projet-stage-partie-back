from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsersSerializer
from Users.models import Users
from django.shortcuts import render, get_object_or_404
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.core.mail import send_mail
import pyotp
from django.conf import settings

from django.shortcuts import get_object_or_404
from django.http import JsonResponse

@api_view(['POST'])
def addUser(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def displayall(request):
    users = Users.objects.all()  # Correct usage of model name
    serializer = UsersSerializer(users, many=True)  # Use serializer instance
    return Response(serializer.data, status=status.HTTP_200_OK) 

    
@api_view(['GET', 'PUT'])
def updateUsers(request, id_user=None):
    user = get_object_or_404(Users, id_user=id_user)
    if request.method == 'PUT':
        serializer = UsersSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data)



@api_view(['DELETE', 'GET'])
def deleteUsers(request, id_user=None):
    if request.method == 'DELETE':
        try:
            user = Users.objects.get(id_user=id_user)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)  # Method not allowed for GET requests

