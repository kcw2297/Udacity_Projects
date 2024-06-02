## Data Engineer

#### [배운점]

- Data Modeling
  - ACID, Normalize vs Denormalize
  - OLAP vs OLTP, Star&Snowflake Schemas
- AWS S3, Redshift

## 음악 데이터 분석을 위한 Star Schema와 ETL 파이프라인 생성

#### [기술스택]

pycopg2, python, pandas

#### [설명]

데이터 분석가가 유저가 듣는 음악의 종류를 분석하려고 합니다. 쿼리를 쉽게 할 수 있도록 </br>
데이터베이스 스키마를 제작하고 ETL 파이프라인을 만듭니다.

#### [데이터 예시]

    {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

#### [스키마]

    Fact Table
    songplays : records in log data associated with song plays i.e. records with page NextSong
    columns : songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

    Dimension Tables
    users : users in the app
    columns : user_id, first_name, last_name, gender, level

    songs : songs in music database
    columns : song_id, title, artist_id, year, duration

    artists : artists in music database
    columns : artist_id, name, location, latitude, longitude

    time : timestamps of records in songplays broken down into specific units
    columns : start_time, hour, day, week, month, year, weekday

## 음악 데이터 분석을 위한 Data Warehouse 제작

#### [기술스택]

pycopg2, python, pandas, AWS(S3, Redshift)

#### [설명]

데이터 분석가가 유저가 듣는 음악의 종류를 분석하려고 합니다. 쿼리를 쉽게 할 수 있도록 </br>
S3에 있는 데이터를 Redshift로 옮기기 위해 데이터베이스 스키마와 ETL 파이프라인을 만듭니다.

#### [데이터 형식]

    Song data: s3://udacity-dend/song_data
    Log data: s3://udacity-dend/log_data

{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
