from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'push_notification.settings')

app = Celery