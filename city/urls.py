from django.urls import path
from city import views


urlpatterns = [
    path('', views.CityList().as_view(), name='city-add-list'),
    path('<int:pk>/', views.CityDetail().as_view(), name='edit-city-detail'),
]