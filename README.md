# Weather App
<br>

## Usage
App manages a collection of cities which can be added and deleted. It provides a functionality to list cities in the collection by either providing <b>city name</b> or the <b>coordinates</b> of the city i.e. <b>Latitude and Longitude</b>. User can search for the current weather of any city from the collection.<br>
Using API service - <a href="https://openweathermap.org/current">OpenWeather API</a> 
<br>

## Technologies Used
- <a href="https://docs.python.org/3/">Python 3.x</a>
- Django (<a href="https://www.django-rest-framework.org/">Django Rest Framework</a>)
- <a href="https://www.postgresql.org/docs/">Postgresql</a>
- <a href="https://docs.celeryproject.org/en/stable/">Celery</a>
- <a href="https://redis.io/documentation">Redis</a>
- <a href="https://docs.docker.com/">Docker</a>
<br>

## Working
You can perform CRUD operations on City Collection and also view weather of any city from the collection using API endpoints provided in postman collection file - <code>WeatherApp.postman_collection.json</code>. 
At the time of creating new entry in city collection we collect the weather of the city and then update the weather of all the cities in the collection using periodic task implemented using celery.
<br>

## Installation and Running
Clone the repository usign command - <code>git clone https://github.com/jatinj615/weather_app.git</code>.<br>
Only prerequisite to run the application is <b>Docker</b>. Install from the official website <a href="https://docs.docker.com/compose/install/">link</a><br>
After installing Docker run the command - <code>docker-compose up -d</code>, to start the application.<br>
To view the logs of the containers, use the command - <code>docker-compose logs</code>.<br>
To close the application, run the command - <code>docker-compose down</code>.

### Unit Tests
Unit tests for the endpoints and API can be found in the given path - <code>base_dir/city/tests/</code>.<br>
Test cases are using <a href="https://docs.python.org/3/library/unittest.mock.html"> Python Mocking</a> for the third party APIs.<br>
To run the unit tests execute the command - <br><code>docker-compose run web python /code/manage.py test city</code>.<br>

### Swagger Documentation

After starting the server, API swagger documentation can be found at the endpoint <code>/api/swagger/</code>. <a href="http://localhost:8000/api/swagger/">link</a>


## Enhancements To Do
Django application uses <b>WSGI</b> server by default which means it can only serve one request at a time which can cause in response delay for concurrent requests made to the application. Therefore, to overcome this scenario we can configure our django application to use <b>uWSGI</b> server which can process multiple requests at once and make changes to docker file accordingly.<br>



