# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lc8_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledscene',
            name='last_date',
            field=models.DateField(null=True, verbose_name='Last Download Date'),
        ),
    ]
