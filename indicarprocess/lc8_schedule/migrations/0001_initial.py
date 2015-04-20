# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledScene',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('path', models.CharField(max_length=3)),
                ('row', models.CharField(max_length=3)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Scheduled Scene',
                'verbose_name_plural': 'Scheduled Scenes',
            },
        ),
    ]
