# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import LandsatListAPI


urlpatterns = patterns('',
    url(r'^landsat/$', LandsatListAPI.as_view(), name='landsat'),
)