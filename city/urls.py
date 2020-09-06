from django.urls import path
from city.views import CityList, WeatherDetailView


city_list = CityList.as_view({
    'get': 'list',
    'post': 'create'
})

city_detail = CityList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

weather_detail = WeatherDetailView.as_view({
    'get': 'list'
})

urlpatterns = [
    path('', city_list, name='city-add-list'),
    path('<int:pk>/', city_detail, name='edit-city-detail'),
    path('<int:pk>/weather/', weather_detail, name='city-weather-detail'),
]