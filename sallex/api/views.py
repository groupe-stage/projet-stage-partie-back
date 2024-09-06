from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SallexSerializer
from sallex.models import Sallex
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def addSallex(request):
    serializer = SallexSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def displayall(request):
    sallex = Sallex.objects.all()
    serializer = SallexSerializer(sallex, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE', 'GET'])
def deleteSallex(request, idse=None):
    if request.method == 'DELETE':
        try:
            sallex = Sallex.objects.get(idse=idse)
            sallex.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Sallex.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)  # Method not allowed for GET requests
