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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.CharField(max_length=255, unique=True)),
                ('path', models.CharField(max_length=500)),
                ('url_tms', models.CharField(max_length=500)),
                ('data', models.DateField()),
                ('shape', django.contrib.gis.db.models.fields.PolygonField(srid=4674, null=True, blank=True)),
            ],
        ),
    ]
