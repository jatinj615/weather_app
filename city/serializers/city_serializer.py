from rest_framework import serializers
from city.models import City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'city_name', 'latitude', 'longitude', 'api_city_id']
        extra_kwargs = {'city_name': {'required': True}}


    def create(self, validated_data):
        city, created = City.objects.update_or_create(
            city_name=validated_data.get('city_name', None),
            latitude=validated_data.get('latitude', None),
            longitude=validated_data.get('longitude', None),
            defaults={'api_city_id': validated_data.get('api_city_id', None)})
        return city, created