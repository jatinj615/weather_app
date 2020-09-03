from rest_framework import generics
from city.serializers import CitySerializer
from city.models import City


class CityList(generics.ListCreateAPIView):
    
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


class CityDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer