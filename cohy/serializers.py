__author__ = 'Rodrigo Paes - rodrigo@ic.ufal.br'

from rest_framework import serializers
from cohy.models import Station


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'code', 'consistency_level', 'date', 'time', 'day_average', 'flow_method',
                  'maximum', 'minimum', 'average', 'day_maximum', 'day_minimum', 'maximum_status',
                  'minimum_status', 'average_status', 'year_average', 'year_average_status', 'flows', 'flows_status')