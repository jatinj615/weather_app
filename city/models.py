from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=100, default='', blank=True)
    latitude = models.CharField(max_length=50, default='', blank=True)
    longitude = models.CharField(max_length=50, default='', blank=True)
    api_city_id = models.CharField(max_length=50, default='', blank=True)


class Weather(models.Model):
    weather_id = models.CharField(max_length=10, default='', blank=True)
    weather_main = models.CharField(max_length=20, default='', blank=True)
    description = models.CharField(max_length=200, default='', blank=True)


class CityWeather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE)
    temperature = models.CharField(max_length=20, default='', blank=True)
    feels_like = models.CharField(max_length=20, default='', blank=True)
    temperature_max = models.CharField(max_length=20, default='', blank=True)
    temperature_min = models.CharField(max_length=20, default='', blank=True)
    pressure = models.CharField(max_length=20, default='', blank=True)
    humidity = models.CharField(max_length=20, default='', blank=True)
    recent = models.BooleanField(default=True)
