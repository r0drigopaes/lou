__author__ = 'Rodrigo Paes - rodrigo@ic.ufal.br'

from django.conf.urls import patterns, url, include
from cohy import views


station_urls = patterns('',
    url(r'^$', views.station_list, name='station_list')
)

urlpatterns = patterns('cohy.views',
    url(r'^$', views.index, name='index'),
    url(r'^stations', include(station_urls)),
)