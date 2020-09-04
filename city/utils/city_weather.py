from city.serializers import CitySerializer
import requests
from django.conf import settings


def get_single_city_weather_info(city_name):
    api_url = settings.CITY_BY_NAME_URL
    params = {'q': city_name,
              'appid': settings.WEATHER_API_KEY}

    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        response = response.json()
        
        city_result = dict(api_city_id=response['id'],
                           city_name=response['name'],
                           latitude=response['coord']['lat'],
                           longitude=response['coord']['lon'])
        
        city_weather = list()
        for weather in response['weather']:
            weather_info = dict(weather_id=weather['id'],
                                weather_main=weather['main'],
                                description=weather['description'])
            city_weather.append(weather_info)
        return city_result, city_weather
    else:
        return None, None


def get_city_by_id_weather(city_ids):
    api_url = settings.CITY_BY_ID_URL
    params = {'id': city_ids,
              'appid': settings.WEATHER_API_KEY}

    response = requests.get(api_url, params=params)
    ## check for status code and bulk update
    