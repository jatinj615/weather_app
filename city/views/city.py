from rest_framework import generics, status
from city.serializers import CitySerializer, WeatherSerializer, CityWeatherSerializer
from city.models import City
from city.utils import get_single_city_weather_info
from rest_framework.response import Response


class CityList(generics.ListCreateAPIView):
    """
    get:
        List all the cities according to the filters
    
    post:
        Create new city collection
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


    def get_queryset(self):
        city_name = self.request.query_params.get('city_name')
        latitude = self.request.query_params.get('latitude')
        longitude = self.request.query_params.get('longitude')

        if city_name is not None:
            queryset = self.queryset.filter(city_name__icontains=city_name)
            return queryset
        elif latitude and longitude is not None:
            queryset = self.queryset.filter(latitude__startswith=latitude, longitude__startswith=longitude)
            return queryset
        else:
            return super().get_queryset()
        
    
    def post(self, request):
        city_name = self.request.data['city_name']
        weather_obj = get_single_city_weather_info(city_name)
        if weather_obj:
            city_serializer = self.get_serializer(data=weather_obj['city_info'])
            city_serializer.is_valid(raise_exception=True)
            city_obj, created = city_serializer.save()
            if created:
                for weather in weather_obj['weather_list']:
                    weather_serializer = WeatherSerializer(data=weather)
                    weather_serializer.is_valid(raise_exception=True)
                    weather_obj = weather_serializer.save()
                    city_weather_serializer = CityWeatherSerializer(data=weather_obj['temperature_details'])
                    city_weather_serializer.is_valid(raise_exception=True)
                    city_weather_serializer.save(city=city_obj, weather=weather_obj)
                return Response(self.get_serializer(city_obj).data, status=status.HTTP_201_CREATED)
            else:
                return Response(self.get_serializer(city_obj).data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'city name not found'}, status=status.HTTP_404_NOT_FOUND)


class CityDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer
