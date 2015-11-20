# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import (LandsatListAPI, RapidEyeListAPI, LandsatDetailView,
    RapidEyeDetailView)


urlpatterns = patterns('',
    url(r'^landsat/$', LandsatListAPI.as_view(), name='landsat'),
    url(r'^rapideye/$', RapidEyeListAPI.as_view(), name='rapideye'),
    url(r'^landsat/(?P<image>[^\s]+)/$', LandsatDetailView.as_view(),
        name='landsat-detail'),
    url(r'^rapideye/(?P<image>[^\s]+)/$', RapidEyeDetailView.as_view(),
        name='rapideye-detail'),
)
