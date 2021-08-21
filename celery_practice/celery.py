from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_practice.settings')

app = Celery('celery_practice')

app.conf.enable_utc = False
app.conf.update(timezone='Europe/Moscow')

app.config_from_object('django.conf:settings', namespace='CELERY')

# celery beat
app.conf.beat_schedule = {
    'send-mail-everyday': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=21, minute=30, day_of_month=16, month_of_year=8)
        #'args': (2,)
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')