from rest_framework.test import APITestCase, APIClient
from city.models import City, Weather, CityWeather
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch, Mock
import json
import os
from city.utils import get_weather_data


ABS_PATH = os.path.dirname(os.path.abspath(__file__))


class TestCityView(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.city_add_list_url = reverse('city-add-list')
        self.city_object = {'city_name': 'delhi',
                            'latitude': '37',
                            'longitude': '90',
                            'api_city_id': '123'}
        city = City.objects.create(**self.city_object)
        self.edit_city_detail_url = reverse('edit-city-detail', args=[city.id])


    @patch('city.utils.city_weather.requests.get')
    def test_store_city_POST(self, mock_get):
        ## Mock the api
        ### read sample json response for api
        json_file = open(ABS_PATH+'/sample_response.json')
        response_obj = json.load(json_file)
        ### Set mock values
        mock_get.return_values = Mock(ok=True)
        mock_get.return_value.status_code = status.HTTP_200_OK
        mock_get.return_value.json.return_value = response_obj

        response = self.client.post(self.city_add_list_url, {'city_name': 'mumbai'})
        ## check for the city name in response with sample json
        self.assertEquals(response.json()['city_name'], response_obj['name'])
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
        response = self.client.put(self.edit_city_detail_url, {'city_name': 'some name'})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    

    def test_city_destroy_DELETE(self):
        response = self.client.delete(self.edit_city_detail_url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
    
    
    def test_city_retrieve_GET(self):
        response = self.client.get(self.edit_city_detail_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    


class TestWeatherView(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.city_object = {'city_name': 'delhi',
                            'latitude': '37',
                            'longitude': '90',
                            'api_city_id': '123'}
        city = City.objects.create(**self.city_object)
        self.city_weather_url = reverse('city-weather-detail', args=[city.id])
    
    
    def test_city_weather_detail_GET(self):
        response = self.client.get(self.city_weather_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
