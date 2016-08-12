# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-11 14:03
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_auto_20151026_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogolandsat',
            name='shape',
        ),
        migrations.AddField(
            model_name='catalogolandsat',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4674),
        ),
    ]