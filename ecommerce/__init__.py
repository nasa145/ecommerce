

# import celery so that to make it gobal available to all apps when django loads
from .celery import app  as celery_app