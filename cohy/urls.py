__author__ = 'Rodrigo Paes - rodrigo@ic.ufal.br'

from django.conf.urls import patterns, url, include
from django.views.i18n import javascript_catalog

from cohy import views

js_info_dict = {
    'packages': ('cohy',),
}


station_urls = patterns('',
    url(r'^/new$', views.station_new, name='station_new'),
    url(r'^/test$', views.test_form, name='station_test')
)

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^stations', views.station_list, name='station_list'),
    url(r'^station', include(station_urls)),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict),
)

#cohy.views