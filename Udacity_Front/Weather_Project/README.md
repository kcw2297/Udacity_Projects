# Weather-Journal App Project
![](project.sample.PNG)

## Overview
Weather Journal App project is to create an asynchronous web app that uses Web API and user data to dynamically update the UI.


### index.html
It contains basic html structures :
-headline
-zip (input)
-textarea (input)
-button (generate)
-placeHolder (result)


### style.css
Color : red, blue, yellow
-red for background
-blue for box
-yellow for text


### server.js
Server side :
Require : express, body-parser, cors
-express for making app instance
-body-parser for easily parse request body
-cors for cross-origin resource sharing

Port listen : 8000

Get route : response send the stored data (weather, date, content)
Post route : store user input and weather data into array


### app.js
Client side :
1. Fetch the data from openweatherapi
2. post the data to the server.js
3. get the data from the sever and insert into html
