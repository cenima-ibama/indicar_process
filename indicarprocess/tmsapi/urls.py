# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import LandsatListAPI, RapidEyeListAPI


urlpatterns = patterns('',
    url(r'^landsat/$', LandsatListAPI.as_view(), name='landsat'),
    url(r'^rapideye/$', RapidEyeListAPI.as_view(), name='rapideye'),
)