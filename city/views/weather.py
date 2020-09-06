from rest_framework import generics, status, viewsets
from city.serializers import CitySerializer, WeatherSerializer, CityWeatherSerializer
from city.models import City, Weather, CityWeather
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class WeatherDetailView(viewsets.ModelViewSet):
    """
    list:
        Get current weather of a particular city from the city collection
        
    """
    queryset = CityWeather.objects.all()
    serializer_class = CityWeatherSerializer

    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def list(self, request, pk):
        city = self.get_object(pk)
        weather_info = CityWeather.objects.filter(city=city, recent=True)
        serializer = self.get_serializer(weather_info, many=True)
        return Response(serializer.data)


