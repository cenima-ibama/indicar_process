# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoRapidEye',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('image', models.CharField(max_length=80, unique=True)),
                ('path', models.CharField(max_length=120)),
                ('tms', models.CharField(max_length=254)),
                ('quicklook', models.CharField(max_length=150)),
                ('data', models.DateField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674, null=True, blank=True)),
                ('nuvens', models.FloatField()),
            ],
            options={
                'db_table': 'catalogo_rapideye',
            },
        ),
    ]
