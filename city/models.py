from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=100, default='', blank=True)
    latitude = models.CharField(max_length=50, default='', blank=True)
    longitude = models.CharField(max_length=50, default='', blank=True)
