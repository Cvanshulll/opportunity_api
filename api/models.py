from django.db import models

# Create your models here.


#Creating opportunity model
class Opportunity(models.Model):
    opportunity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.TextField()
    batch = models.CharField(max_length=100)
    job_id = models.CharField(max_length=100)
    job_link = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    end_date = models.DateField(default='', blank=True)
    description = models.TextField()
    stipend = models.CharField(max_length=100)
    added_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # image = models.ImageField(upload_to='opportunity_images')

