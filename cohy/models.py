from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


def to_float(value):
    try:
        return float(value)
    except ValueError:
        return None


def to_int(value):
    try:
        return int(value)
    except ValueError:
        return None


def create_station(line_array):
    s = Station()
    s.code = line_array[0]
    s.consistency_level = to_int(line_array[1])
    try:
        s.date = datetime.strptime(line_array[2], '%d/%m/%Y').date()
    except ValueError:
        s.date = None
    try:
        s.time = datetime.strptime(line_array[3], '%H:%M')
    except ValueError:
        s.time = None
    s.day_average = True if to_int(line_array[4]) == 1 else False
    s.flow_method = to_int(line_array[5])
    s.maximum = to_float(line_array[6].replace(',', '.'))
    s.minimum = to_float(line_array[7].replace(',', '.'))
    s.average = to_float(line_array[8].replace(',', '.'))
    s.day_maximum = to_int(line_array[9])
    s.day_minimum = to_int(line_array[10])
    s.maximum_status = to_int(line_array[11])
    s.minimum_status = to_int(line_array[12])
    s.average_status = to_int(line_array[13])

    s.year_average = to_float(line_array[14].replace(',', '.'))
    s.year_average_status = to_int(line_array[15])

    flows = line_array[16].replace(',', '.')
    flows_status = line_array[47].replace(',', '.')
    for i in range(17, 78):
        if i < 47:
            flows += ',' + (line_array[i].replace(',', '.'))
        elif i > 47:
            flows_status += ',' + (line_array[i].replace(',', '.'))

    s.flows = str(flows)
    s.flows_status = str(flows_status)

    return s


# Create your models here.
class Station(models.Model):
    CONSISTENCY_RAW = 1
    CONSISTENCY_CONSISTED = 2
    CONSISTENCY_CHOICES = (
        (CONSISTENCY_RAW, _('bruto')),
        (CONSISTENCY_CONSISTED, _('consistido'))
    )

    #1 = Curva de descarga, 2 = Transfer�ncia de vaz�es, 3 = Soma de vaz�es, 4 = ADCP
    FLOW_METHOD_UNLOAD = 1
    FLOW_METHOD_TRANSFER = 2
    FLOW_METHOD_SUM = 3
    FLOW_METHOD_ADCP = 4
    FLOW_METHOD_CHOICES = (
        (FLOW_METHOD_UNLOAD, _('flow_method_unload')),
        (FLOW_METHOD_TRANSFER, _('flow_method_transfer')),
        (FLOW_METHOD_SUM, _('flow_method_sum')),
        (FLOW_METHOD_ADCP, _('flow_method_adcp'))
    )

    #Status: 0 = Branco, 1 = Real, 2 = Estimado, 3 = Duvidoso, 4 = R�gua Seca
    STATUS_WHITE = 0
    STATUS_REAL = 1
    STATUS_ESTIMATED = 2
    STATUS_UNCERTAIN = 3
    STATUS_DRY = 4

    STATUS_CHOICES = (
        (STATUS_WHITE, _('status_white')),
        (STATUS_REAL, _('status_real')),
        (STATUS_ESTIMATED, _('status_estimated')),
        (STATUS_UNCERTAIN, _('status_uncertain')),
        (STATUS_DRY, _('status_dry'))
    )

    code = models.CharField(max_length=15)
    consistency_level = models.IntegerField(choices=CONSISTENCY_CHOICES, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    day_average = models.NullBooleanField()
    flow_method = models.IntegerField(choices=FLOW_METHOD_CHOICES, null=True)
    maximum = models.FloatField(null=True)
    minimum = models.FloatField(null=True)
    average = models.FloatField(null=True)
    day_maximum = models.IntegerField(null=True)
    day_minimum = models.IntegerField(null=True)
    maximum_status = models.IntegerField(choices=STATUS_CHOICES, null=True)
    minimum_status = models.IntegerField(choices=STATUS_CHOICES, null=True)
    average_status = models.IntegerField(choices=STATUS_CHOICES, null=True)
    year_average = models.FloatField(null=True)
    year_average_status = models.IntegerField(choices=STATUS_CHOICES, null=True)

    # As vazões estão armazenadas como texto. Logo os cálculos devem ser
    # feitos via aplicação e não no banco.
    flows = models.TextField(max_length=300, null=True)
    flows_status = models.TextField(max_length=100, null=True)

    # Transient fields
    flows_as_list = None
    flows_status_as_list = None

    def get_flow(self, index):
        if not self.flows_as_list:
            self.flows_as_list = [to_float(x) for x in self.flows.split(',')]
        return self.flows_as_list[index]

    def get_flow_status(self, index):
        if not self.flows_status_as_list:
            self.flows_status_as_list = [to_float(x) for x in self.flows_status.split(',')]
        return self.flows_status_as_list[index]




