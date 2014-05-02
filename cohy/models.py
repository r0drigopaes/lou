from django.db import models
from django.utils.translation import ugettext_lazy as _
from time import *

MAX_DESCRIPTION_SIZE = 15000

def create_station(line_array):
    s = Station()
    s.code = line_array[0]
    s.consistency_level = int(line_array[1])
    s.date = strptime(line_array[2], '%d/%m/%Y')
    '''time = models.TimeField(blank=True)
    day_average = models.BooleanField()
    flow_method = models.IntegerField(choices=FLOW_METHOD_CHOICES)
    maximum = models.FloatField()
    minimum = models.FloatField()
    average = models.FloatField()
    day_maximum = models.IntegerField()
    day_minimum = models.IntegerField()
    maximum_status = models.IntegerField(choices=STATUS_CHOICES)
    minimum_status = models.IntegerField(choices=STATUS_CHOICES)
    average_status = models.IntegerField(choices=STATUS_CHOICES)
    year_average = models.FloatField()
    year_average_status = models.IntegerField(choices=STATUS_CHOICES)
    '''
    #TODO: popular os outros atributos do objeto
    return s

# Create your models here.
class Station(models.Model):
    CONSISTENCY_RAW = 1
    CONSISTENCY_CONSISTED = 2
    CONSISTENCY_CHOICES = (
        (CONSISTENCY_RAW, _('bruto')),
        (CONSISTENCY_CONSISTED,_('consistido'))
    )

    #1 = Curva de descarga, 2 = Transfer�ncia de vaz�es, 3 = Soma de vaz�es, 4 = ADCP
    FLOW_METHOD_UNLOAD = 1
    FLOW_METHOD_TRANSFER = 2
    FLOW_METHOD_SUM = 3
    FLOW_METHOD_ADCP = 4
    FLOW_METHOD_CHOICES = (
        (FLOW_METHOD_UNLOAD,_('flow_method_unload')),
        (FLOW_METHOD_TRANSFER,_('flow_method_transfer')),
        (FLOW_METHOD_SUM,_('flow_method_sum')),
        (FLOW_METHOD_ADCP,_('flow_method_adcp'))
    )

    #Status: 0 = Branco, 1 = Real, 2 = Estimado, 3 = Duvidoso, 4 = R�gua Seca
    STATUS_WHITE = 0
    STATUS_REAL = 1
    STATUS_ESTIMATED = 2
    STATUS_UNCERTAIN = 3
    STATUS_DRY = 4

    STATUS_CHOICES = (
        (STATUS_WHITE,_('status_white')),
        (STATUS_REAL,_('status_real')),
        (STATUS_ESTIMATED,_('status_estimated')),
        (STATUS_UNCERTAIN,_('status_uncertain')),
        (STATUS_DRY,_('status_dry'))
    )


    code = models.CharField(max_length=15)
    consistency_level = models.IntegerField(choices=CONSISTENCY_CHOICES)
    date = models.DateField()
    time = models.TimeField(blank=True)
    day_average = models.BooleanField()
    flow_method = models.IntegerField(choices=FLOW_METHOD_CHOICES)
    maximum = models.FloatField()
    minimum = models.FloatField()
    average = models.FloatField()
    day_maximum = models.IntegerField()
    day_minimum = models.IntegerField()
    maximum_status = models.IntegerField(choices=STATUS_CHOICES)
    minimum_status = models.IntegerField(choices=STATUS_CHOICES)
    average_status = models.IntegerField(choices=STATUS_CHOICES)
    year_average = models.FloatField()
    year_average_status = models.IntegerField(choices=STATUS_CHOICES)
    # TODO: como armazenar as vazões? São 32 floats, cada um com um status.

    #Vazao01Status;Vazao02Status;Vazao03Status;Vazao04Status;Vazao05Status;Vazao06Status;Vazao07Status;Vazao08Status;Vazao09Status;Vazao10Status;Vazao11Status;Vazao12Status;Vazao13Status;Vazao14Status;Vazao15Status;Vazao16Status;Vazao17Status;Vazao18Status;Vazao19Status;Vazao20Status;Vazao21Status;Vazao22Status;Vazao23Status;Vazao24Status;Vazao25Status;Vazao26Status;Vazao27Status;Vazao28Status;Vazao29Status;Vazao30Status;Vazao31Status;