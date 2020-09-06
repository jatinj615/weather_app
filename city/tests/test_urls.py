from rest_framework.test import APISimpleTestCase
from django.urls import reverse, resolve
from city.views import CityList, WeatherDetailView


class TestUrls(APISimpleTestCase):

    def test_city_add_list_url(self):
        url = reverse('city-add-list')
        self.assertEquals(resolve(url).func.cls, CityList)
    

    def test_city_edit_details_url(self):
        url = reverse('edit-city-detail', args=[1])
        self.assertEquals(resolve(url).func.cls, CityList)


    def test_weather_add_url(self):
        url = reverse('city-weather-detail', args=[1])
        self.assertEquals(resolve(url).func.cls, WeatherDetailView)