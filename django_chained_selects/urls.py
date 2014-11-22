# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.conf.urls import patterns, url
from django_chained_selects.views import FilterChainView


urlpatterns = patterns(
    '',
    url(r'^(?P<app_name>[\w\-]+)/(?P<model_name>[\w\-]+)/'
        r'(?P<method_name>[\w\-]+)/(?P<pk>[\$\w\-]+)/$',
        FilterChainView.as_view(),
        name='filter_all'),
    url(r'^(?P<app_name>[\w\-]+)/(?P<model_name>[\w\-]+)/(?P<pk>[\$\w\-]+)/$',
        FilterChainView.as_view(),
        name='filter_all'),
)
