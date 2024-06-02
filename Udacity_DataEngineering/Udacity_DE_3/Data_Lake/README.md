# Project: Data Lake 

### Introduction
A music streaming startup, Sparkify, has grown their user base and song database even more and want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow their analytics team to continue finding insights in what songs their users are listening to.

You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

### Project Datasets
Song data: s3://udacity-dend/song_data
Log data: s3://udacity-dend/log_data

visit : https://s3.console.aws.amazon.com/s3/buckets/udacity-dend


### Schema for Song Play Analysis

#### Fact Table
1. songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

#### Dimension Tables
2. users - users in the app
user_id, first_name, last_name, gender, level

3. songs - songs in music database
song_id, title, artist_id, year, duration

4. artists - artists in music database
artist_id, name, location, lattitude, longitude

5. time - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday


### Project Template
etl.py - reads data from S3, processes that data using Spark, and writes them back to S3
dl.cfg - contains your AWS credentials
README.md - provides discussion on your process and decisions