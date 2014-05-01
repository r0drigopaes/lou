from django.test import TestCase
from cohy.models import Station
import common.util as util
import os

# Create your tests here.

class StationTests(TestCase):
    def test_read_csv(self):
        strpath = os.path.join( os.path.dirname(__file__),'resources','44630000.TXT')
        util.read_csv(strpath)
        pass