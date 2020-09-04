from rest_framework import generics, status
from city.serializers import CitySerializer, WeatherSerializer, CityWeatherSerializer
from city.models import City, Weather, CityWeather
from city.utils import get_single_city_weather_info
from rest_framework.response import Response


class WeatherDetailView(generics.RetrieveAPIView):

    queryset = CityWeather.objects.all()
    serializer_class = CityWeatherSerializer


    def get(self, request, pk):
        city = City.objects.get(pk=pk)
        weather_info = CityWeather.objects.filter(city=city, recent=True)
        serializer = self.get_serializer(weather_info, many=True)
        return Response(serializer.data)


