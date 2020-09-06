from rest_framework import generics, status, viewsets
from city.serializers import CitySerializer, WeatherSerializer, CityWeatherSerializer
from city.models import City
from city.utils import get_single_city_weather_info
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class CityList(viewsets.ModelViewSet):
    """
    list:
        List all the cities or search by city name or latitude & longitude filter
        from city collection

    create:
        Insert new city information in the city collection
    
    retrieve:
        Get information of a single city from the city collection

    update:
        Update information of a particular city in the city collection
    
    destroy:
        Delete particula city information from the city collection
    """
    
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_object(self, pk):
        try:
            return self.queryset.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404


    def get_queryset(self):
        city_name = self.request.query_params.get('city_name', None)
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        if city_name:
            city_name=str(city_name)
            queryset = self.queryset.filter(city_name__icontains=city_name)
            return queryset
        elif latitude and longitude:
            latitude = str(latitude)
            longitude = str(longitude)
            queryset = self.queryset.filter(latitude__startswith=latitude, longitude__startswith=longitude)
            return queryset
        else:
            return super().get_queryset()
    

    def create(self, request):
        city_name = str(self.request.data['city_name'])
        weather_res = get_single_city_weather_info(city_name)
        if weather_res:
            city_serializer = self.get_serializer(data=weather_res['city_info'])
            city_serializer.is_valid(raise_exception=True)
            city_obj, created = city_serializer.save()
            temperature = weather_res
            if created:
                for weather in weather_res['weather_list']:
                    weather_serializer = WeatherSerializer(data=weather)
                    weather_serializer.is_valid(raise_exception=True)
                    weather_obj = weather_serializer.save()
                    city_weather_serializer = CityWeatherSerializer(data=weather_res['temperature_details'])
                    city_weather_serializer.is_valid(raise_exception=True)
                    city_weather_serializer.save(city=city_obj, weather=weather_obj)
                return Response(self.get_serializer(city_obj).data, status=status.HTTP_201_CREATED)
            else:
                return Response(self.get_serializer(city_obj).data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'city name not found'}, status=status.HTTP_404_NOT_FOUND)


    def update(self, request, pk):
        instance = self.get_object(pk)
        serializer = self.get_serializer(instance, data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk):
        instance = self.get_object(pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
