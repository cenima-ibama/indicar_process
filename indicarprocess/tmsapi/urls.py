# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import (LandsatListAPI, RapidEyeListAPI, LandsatDetailView,
    RapidEyeDetailView)


app_name = 'tmsapi'

urlpatterns = [
    url(r'^landsat/$', LandsatListAPI.as_view(), name='landsat'),
    url(r'^rapideye/$', RapidEyeListAPI.as_view(), name='rapideye'),
    url(r'^landsat/(?P<image>[^\s]+)/$', LandsatDetailView.as_view(),
        name='landsat-detail'),
    url(r'^rapideye/(?P<image>[^\s]+)/$', RapidEyeDetailView.as_view(),
        name='rapideye-detail'),
]
