from rest_framework import serializers
from city.models import CityWeather
from city.serializers import WeatherSerializer


class CityWeatherSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.city_name', read_only=True)
    weather = WeatherSerializer(read_only=True)

    class Meta:
        model = CityWeather
        fields = ['city', 'weather', 'temperature', 'feels_like',
                  'temperature_max', 'temperature_min', 'pressure', 'humidity']
    
    