from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Salle.models import Salle
from .serializers import SalleSerializer

@api_view(['POST'])
def addSalle(request):
    serializer = SalleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def displayAllSalles(request):
    salles = Salle.objects.all()
    serializer = SalleSerializer(salles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
def updateSalle(request, id_salle=None):
    salle = get_object_or_404(Salle, id_salle=id_salle)
    if request.method == 'PUT':
        serializer = SalleSerializer(instance=salle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = SalleSerializer(salle)
        return Response(serializer.data)

@api_view(['DELETE', 'GET'])
def deleteSalle(request, id_salle=None):
    if request.method == 'DELETE':
        try:
            salle = Salle.objects.get(id_salle=id_salle)
            salle.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Salle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
