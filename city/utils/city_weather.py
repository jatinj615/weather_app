from city.serializers import CitySerializer
import requests
from django.conf import settings
from city.models import Weather, CityWeather, City


def get_weather_data(city_name=None, city_id=None):
    api_url = settings.SINGLE_CITY_URL
    params = {'appid': settings.WEATHER_API_KEY}
    
    if city_name:
        params['q'] = city_name
    elif city_id:
        params['id'] = city_id
    else:
        return False

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return False


def get_single_city_weather_info(city_name):
    response = get_weather_data(city_name=city_name)
    if response:
        city_result = dict(api_city_id=response['id'],
                           city_name=response['name'],
                           latitude=response['coord']['lat'],
                           longitude=response['coord']['lon'])
        
        city_weather_list = list()
        for weather in response['weather']:
            weather_info = dict(weather_id=weather['id'],
                                weather_main=weather['main'],
                                description=weather['description'])
            city_weather_list.append(weather_info)
        return city_result, city_weather_list
    else:
        return None, None


def get_city_weather_by_id():
    weather_list_obj = list()
    cities = City.objects.all()
    for city in cities:
        city_id = city.api_city_id
        response = get_weather_data(city_id=city_id)
        if response:
            for weather in response['weather']:
                weather_obj = Weather.objects.get_or_create(weather_id=weather['id'],
                                                            weather_main=weather['main'],
                                                            description=weather['description'])
                city_weather_obj = CityWeather(city=city, weather=weather_obj)
                weather_list_obj.append(city_weather_obj)
        else:
            return False

    return weather_list_obj
        
    