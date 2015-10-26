# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20151009_0929'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='catalogolandsat',
            table='img_catalogo_landsat_a',
        ),
        migrations.AlterModelTable(
            name='catalogorapideye',
            table='img_catalogo_rapideye_a',
        ),
    ]
