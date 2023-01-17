"""
ASGI config for opportunityapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/

from django.db import models

# Create your models here.

#Creating opportunity model
class Opportunity(models.Model):
    opportunity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.TextField(default='')
    batch = models.CharField(max_length=100, default='Everyone')
    job_id = models.CharField(max_length=100, default='')
    job_link = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=100, default='')
    end_date = models.DateField(default='', blank=True)
    description = models.TextField(default='No description provided', blank=True)
    stipend = models.CharField(max_length=100, default='')
    added_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # image = models.ImageField(upload_to='opportunity_images')

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opportunityapi.settings')

application = get_asgi_application()
