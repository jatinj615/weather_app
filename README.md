# Weather App
<br>

## Usage
App manages a collection of cities which can be added and deleted. It provides a functionality to list cities in the collection by either providing <b>city name</b> or the <b>coordinates</b> of the city i.e. <b>Latitude and Longitude</b>. User can search for the current weather of any city from the collection.<br>
Using API service - <a href="https://openweathermap.org/current" target="_blank">OpenWeather API</a> 
<br>

## Technologies Used
- <a href="https://docs.python.org/3/" target="_blank">Python 3.x</a>
- Django (<a href="https://www.django-rest-framework.org/" target="_blank">Django Rest Framework</a>)
- <a href="https://www.postgresql.org/docs/" target="_blank">Postgresql</a>
- <a href="https://docs.celeryproject.org/en/stable/" target="_blank">Celery</a>
- <a href="https://redis.io/documentation" target="_blank">Redis</a>
- <a href="https://docs.docker.com/" target="_blank">Docker</a>
<br>

## Working
APP can perform CRUD operations on City Collection and also view weather of any city from the collection using API endpoints provided in postman collection file - 
```
- BASE_DIR/WeatherApp.postman_collection.json
```
At the time of creating new entry in city collection we collect the weather of the city and then update the weather of all the cities in the collection using periodic task implemented using celery.
<br>

## Installation and Running
Only prerequisite to run the application is <b>Docker</b>. Install from the official website <a href="https://docs.docker.com/compose/install/" target="_blank">link</a><br>

Instructions to run the application - 
```
- git clone https://github.com/jatinj615/weather_app.git      ## Clone the repository
- cd weather_app/                                             ## Change working directory
- docker-compose up -d                                        ## Start the docker container
```
To view the logs of the containers - 
```
- docker-compose logs
```
To close the application - 
```
- docker-compose down
```



### Unit Tests
Unit tests for the endpoints and API can be found in the given path - 
```
- BASE_DIR/city/tests/
```
Test cases are using <a href="https://docs.python.org/3/library/unittest.mock.html" target="_blank"> Python Mocking</a> for the third party APIs.<br>
To run the unit tests - 
```
- docker-compose run web python /code/manage.py test city
```

### Swagger Documentation

API swagger documentation can be found at the <a href="https://app.swaggerhub.com/apis/jatinj6159/weather-app/1.0.0#/" target="_blank">link</a>


## Enhancements To Do
Django application uses <b>WSGI</b> server by default which means it can only serve one request at a time which can cause in response delay for concurrent requests made to the application. Therefore, to overcome this scenario we can configure our django application to use <b>uWSGI</b> server which can process multiple requests at once and make changes to docker file accordingly.<br>



