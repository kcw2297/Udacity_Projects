# Project: Data Warehouse

### Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.


## Data Warehouse Schemas

### Song Data
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null
, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", 
"title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

### Staging Table
staging_events - staging log data ; artist, auth, firstName, gender, itemINSession, lastName, length, level, location, method, page, registration, sessionId, song, status, ts, userAgent, userId
staging_songs - staging song data ; num_songs, arist_id, artist_latitude, artist_longitude, artist_location, artist_name, song_id, title, duration, year

### Fact Table
songplays - records in event data associated with song plays i.e. records with page NextSong ; songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables
users - users in the app ; user_id, first_name, last_name, gender, level
songs - songs in music database ; song_id, title, artist_id, year, duration
artists - artists in music database ; artist_id, name, location, lattitude, longitude
time - timestamps of records in songplays broken down into specific units ; start_time, hour, day, week, month, year, weekday