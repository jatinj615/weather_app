from city.models import City
from city.serializers import CitySerializer
import requests
from django.conf import settings


def get_single_city_weather_info(city_name):
    api_url = settings.CITY_BY_NAME_URL
    params = {'q': city_name,
              'api_key': settings.WEATHER_API_KEY}

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        response = response.json()
        city_result = dict(city_name=response['name'],
                           latitude=response['coord']['lat'],
                           longitude=latitude=response['coord']['lon'])
        
        return city_result
    else:
        return None


def get_city_by_id_weather(city_ids):
    api_url = settings.CITY_BY_ID_URL
    params = {'id': city_ids,
              'api_key': settings.WEATHER_API_KEY}

    response = requests.get(api_url, params=params)
    ## check for status code and bulk update
    