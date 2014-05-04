__author__ = 'Rodrigo Paes - rodrigo@ic.ufal.br'

from django.conf.urls import patterns, url
from cohy import views

urlpatterns = patterns('cohy.views',
    url(r'^$', views.index, name='index'),
    url(r'^angular/$', views.angular, name='angular'),
    url(r'^myobjects/$', views.get_my_objects, name='get_my_objects'),
    url(r'^list/$', views.station_list, name='station_list'),
)