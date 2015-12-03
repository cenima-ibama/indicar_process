# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView


app_name = 'catalogo'

urlpatterns = [
    url(r'^recursos/$',
        TemplateView.as_view(template_name='catalogo/recursos.html'),
        name='resources'),
]