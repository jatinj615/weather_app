from rest_framework.test import APITestCase, APIClient
from city.models import City, Weather, CityWeather
from django.urls import reverse
from rest_framework import status


class TestCityView(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.city_add_list_url = reverse('city-add-list')
        self.edit_city_detail_url = reverse('edit-city-detail', args=[1])
        self.city_object = {'city_name': 'delhi',
                            'latitude': '37',
                            'longitude': '90',
                            'api_city_id': '123'}
        self.weather_object = {'weather_id': '200',
                               'weather_main': 'clean',
                               'description': 'clean'}
        

    
    def test_store_city_POST(self):
        response = self.client.post(self.city_add_list_url, {'city_name': 'delhi'})
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_city_GET(self):
        ## without param
        response = self.client.get(self.city_add_list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        ## with city name param
        response = self.client.get(self.city_add_list_url, {'city_name': 'example_city'})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
        ## with latitude and longitude param
        response = self.client.get(self.city_add_list_url, {'latitude': 'some_value', 'longitude': 'some_value'})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_city_update_PUT(self):
        City.objects.create(**self.city_object)
        response = self.client.put(self.edit_city_detail_url, {'city_name': 'some name'})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_city_destroy_DELETE(self):
        City.objects.create(**self.city_object)
        response = self.client.delete(self.edit_city_detail_url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_city_retrieve_GET(self):
        City.objects.create(**self.city_object)
        response = self.client.get(self.edit_city_detail_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    


class TestWeatherView(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.city_weather_url = reverse('city-weather-detail', args=[1])
        self.city_object = {'city_name': 'delhi',
                            'latitude': '37',
                            'longitude': '90',
                            'api_city_id': '123'}
    
    
    def test_city_weather_detail_GET(self):
        City.objects.create(**self.city_object)
        response = self.client.get(self.city_weather_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        


