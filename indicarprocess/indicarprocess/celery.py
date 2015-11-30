# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'indicarprocess.settings.local')

app = Celery('indicarprocess', backend='rpc://', broker='amqp://guest:guest@localhost:5672//')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=0,
    CELERYBEAT_SCHEDULE={
        'download': {
            'task': 'imagery.tasks.download_all',
            'schedule': crontab(minute=0, hour='2')
        },
        'download_requests': {
            'task': 'imagery.tasks.download_all_scene_requests',
            'schedule': crontab(minute=0, hour='21')
        },
        'process': {
            'task': 'imagery.tasks.process_all',
            'schedule': crontab(minute=30, hour='5,13,22')
        },
        'not_found_scenes_alert': {
            'task': 'imagery.tasks.not_found_scenes_alert',
            'schedule': crontab(minute=59, hour='23')
        },
    },
)

if __name__ == '__main__':
    app.start()