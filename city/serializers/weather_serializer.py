from rest_framework import serializers
from city.models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = ['weather_id', 'weather_main', 'description']

    def create(self, validated_data):
        weather, created = Weather.objects.update_or_create(
            weather_main=validated_data.get('weather_main', None),
            description=validated_data.get('description', None),
            defaults={'weather_id': validated_data.get('weather_id', None)})
        return weather

