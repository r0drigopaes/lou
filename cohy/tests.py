from django.test import TestCase
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from cohy.models import Station
from cohy.models import create_station
import common.util as util
import os
from datetime import datetime
from cohy.serializers import StationSerializer
from rest_framework.compat import BytesIO


# Create your tests here.



class UtilTests(TestCase):
    def test_read_csv(self):
        strpath = os.path.join(os.path.dirname(__file__), 'resources', '44630000.TXT')
        util.read_csv(strpath, 17)
        pass


class StationTests(TestCase):
    ana_station_file = None

    def setUp(self):
        self.ana_station_file = os.path.join(os.path.dirname(__file__), 'resources', '44630000.TXT')
        self.test_station_file = os.path.join(os.path.dirname(__file__), 'resources', 'test_station.TXT')

    def test_load_to_object(self):
        test_stations = util.read_csv(self.test_station_file, 17)
        a_station = create_station(test_stations[1])
        self.assertEqual(1.1, a_station.get_flow(0))
        self.assertEqual(31.31, a_station.get_flow(30))
        self.assertEqual(datetime.strptime('1/2/2006', '%d/%m/%Y').date(), a_station.date)

        self.assertEqual(1, a_station.get_flow_status(0))
        self.assertEqual(1, a_station.get_flow_status(1))
        self.assertEqual(0, a_station.get_flow_status(2))
        self.assertEqual(0, a_station.get_flow_status(3))

        self.assertEqual(1, a_station.get_flow_status(27))
        self.assertEqual(0, a_station.get_flow_status(28))
        self.assertEqual(1, a_station.get_flow_status(29))
        self.assertEqual(0, a_station.get_flow_status(30))
        a_station.save()

        a_station = create_station(test_stations[2])
        a_station.save()

        all_csv_stations = util.read_csv(self.ana_station_file, 17)
        for a__csv_station in all_csv_stations:
            a_station = create_station(a__csv_station)
            self.assertIsNotNone(a_station)
            a_station.save()

class StationSerializerTest(TestCase):
    def setUp(self):
        self.test_station_file = os.path.join(os.path.dirname(__file__), 'resources', 'test_station.TXT')

    def test_serializer(self):
        test_stations = util.read_csv(self.test_station_file, 17)
        a_station = create_station(test_stations[1])
        a_station.save()
        print(a_station.pk)
        ser = StationSerializer(a_station)
        content = JSONRenderer().render(ser.data)
        self.assertIsNotNone(content)
        stream = BytesIO(content)
        data = JSONParser().parse(stream)

        ser = StationSerializer(data=data)
        self.assertTrue(ser.is_valid())