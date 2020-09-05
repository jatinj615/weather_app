# Weather App
<br>

## Usage
***
App manages a collection of cities which can be added and deleted. It provides a functionality to list cities in the collection by either providing <b>city name</b> or the <b>coordinates</b> of the city i.e. <b>Latitude and Longitude</b>. User can search for the current weather of any city from the collection.<br>
Using API service - <a href="https://openweathermap.org/current">OpenWeather API</a> 
<br>

## Technologies Used
***
- <a href="https://docs.python.org/3/">Python 3.x</a>
- Django (<a href="https://www.django-rest-framework.org/">Django Rest Framework</a>)
- <a href="https://www.postgresql.org/docs/">Postgresql</a>
- <a href="https://docs.celeryproject.org/en/stable/">Celery</a>
- <a href="https://redis.io/documentation">Redis</a>
- <a href="https://docs.docker.com/">Docker</a>
<br>

## Working
***
You can perform CRUD operations on City Collection and also view weather of any city from the collection using API endpoints provided in postman collection file - <code>WeatherApp.postman_collection.json</code>. 
At the time of creating new entry in city collection we collect the weather of the city and then update the weather of all the cities in the collection using periodic task implemented using celery.
<br>

## Installation and Running
***
Only prerequisite to run the application is <b>Docker</b> from the Installation <a href="https://docs.docker.com/compose/install/">link</a><br>
After installing Docker run the command <code>docker-compose up</code>



