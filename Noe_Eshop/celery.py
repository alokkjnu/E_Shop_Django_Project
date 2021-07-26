import os
from celery import Celery
from django.conf import settings

# set the default django setting module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Noe_Eshop.settings')

app = Celery('Noe_Eshop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
