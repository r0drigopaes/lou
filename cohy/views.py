from django.conf import settings
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import os
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser

from cohy.models import Station, create_station
from cohy.serializers import StationSerializer

from django.core.files.storage import default_storage

import time


import json
import sys

# Create your views here.
from common import util


def index(request):
    return render(request, 'cohy/index.html')


@api_view(['GET'])
def get_my_objects(request, format=None):
    if request.method == 'GET':
        myobjects = [{'name': 'Rodrigo Paes'}, {'name': 'Taíse Carvalho'}]
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

@api_view(['POST'])
def test_form(request, format=None):
    print('test_form: '+str(request.DATA['name']))
    field = {'name': 'um nome do servidor', 'desc': 'sucesso'}
    return Response(field)

#TODO falta realizar todas as validações.
@api_view(['POST'])
@parser_classes((MultiPartParser,))
def station_new(request, format=None):
    print('encontrou!!')
    print(request.FILES)
    try:
        data = request.FILES['file']
        path = default_storage.save('tmp/stations_temp.txt', ContentFile(data.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)


        test_stations = util.read_csv(tmp_file, 17)
        print("Reading "+str(len(test_stations)))
        #TODO muito lento, trocar por um 'bulk insert' ou algo do tipo
        for a_line in test_stations:
            station = create_station(a_line)
            station.save()

        print("deu certo")

    except:
        print("deu pau")
        print( sys.exc_info())


    msg = {'name': 'um nome do servidor', 'desc': 'sucesso'}
    return Response(msg)
