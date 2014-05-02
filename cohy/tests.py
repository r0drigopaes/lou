from django.test import TestCase
from cohy.models import Station
from cohy.models import create_station
import common.util as util
import os

# Create your tests here.



class UtilTests(TestCase):
    def test_read_csv(self):
        strpath = os.path.join( os.path.dirname(__file__),'resources','44630000.TXT')
        util.read_csv(strpath,17)
        pass

class StationTests(TestCase):
    strpath = None

    def setUp(self):
        self.strpath = os.path.join( os.path.dirname(__file__),'resources','44630000.TXT')

    def test_load_to_object(self):
        all_csv_stations = util.read_csv(self.strpath,17)
        for a_station in all_csv_stations:
            self.assertIsNotNone(create_station(a_station))