from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KVproject.settings')

app = Celery('KVproject',
             broker='pyamqp://guest@localhost//', # 'redis://localhost:6379/0'
             #backend='redis://localhost',
             include=['KVproject.tasks'])
app.conf.CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

if __name__ == '__main__':
    app.start()