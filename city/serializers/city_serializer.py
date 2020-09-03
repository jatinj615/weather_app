from rest_framework import serializers
from city.models import City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'city_name', 'latitude', 'longitude']
        extra_kwargs = {'city_name': {'required': True}}

