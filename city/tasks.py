import structlog
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from city.utils import get_city_weather_by_id
from city.models import CityWeather


def update_city_weather():
    weather_list_obj = get_city_weather_by_id()
    if not weather_list_obj == None:
        try:
            CityWeather.objects.all().delete()
            CityWeather.objects.bulk_create(weather_list_obj)
            response = dict(message='Refreshed Database for weather')
            return response
        except Exception as e:
            response = dict(error=str(e))
            return response
    else:
        response = dict(error='API Downtime')



