from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Registration.settings')

app = Celery('Django_Registration')

app.config_from_object('django.conf:settings')
# app.autodiscover_tasks()
app.conf.beat_schedule = {
    'every-1-seconds': {
        'task': 'todo.tasks.hello_world',
        'schedule': 1,
        'args': (['self'],)
    },
}
app.autodiscover_tasks()

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.conf.timezone = 'UTC'
