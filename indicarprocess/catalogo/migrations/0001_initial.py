# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoLandsat',
            fields=[
                ('objectid', models.AutoField(serialize=False, primary_key=True)),
                ('image', models.CharField(max_length=255, unique=True)),
                ('path', models.CharField(max_length=500)),
                ('url_tms', models.CharField(max_length=500)),
                ('data', models.DateField()),
                ('shape', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4674)),
            ],
            options={
                'db_table': 'catalogo_landsat',
            },
        ),
    ]
