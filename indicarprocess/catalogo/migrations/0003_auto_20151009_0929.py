# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_catalogorapideye'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogolandsat',
            name='nuvens',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='catalogolandsat',
            name='orbita',
            field=models.CharField(null=True, max_length=3),
        ),
        migrations.AddField(
            model_name='catalogolandsat',
            name='ponto',
            field=models.CharField(null=True, max_length=3),
        ),
        migrations.AddField(
            model_name='catalogolandsat',
            name='quicklook',
            field=models.CharField(null=True, max_length=150),
        ),
    ]
