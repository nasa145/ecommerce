
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINS_MODULE', 'ecommerce.settings')

app = Celery('ecommerce')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()