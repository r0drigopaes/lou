from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cohy.models import Station
from cohy.serializers import StationSerializer

import json

# Create your views here.

def index(request):
    return render(request, 'cohy/index.html')


def angular(request):
    return render(request, 'cohy/list.html')


@api_view(['GET'])
def get_my_objects(request, format=None):
    if request.method == 'GET':
        myobjects = [{'name': 'Rodrigo Paes'},{'name':'Taíse Carvalho'}]
        return Response(myobjects)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def station_list(request, format=None):
    if request.method == 'GET':
        stations = Station.objects.all()
        serializer = StationSerializer(stations, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
