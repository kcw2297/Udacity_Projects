## Data Dictionary

#### Fact Table - This data is from immigration_data.csv
fact_id SERIAL PRIMARY KEY, 
cicid INT,
state VARCHAR,
country VARCHAR,
year INT,
month INT


#### People Dimensional Table - This data is from immigration_data.csv
people_id SERIAL PRIMARY KEY, 
cicid INT,
citizen VARCHAR,
resident VARCHAR,
age INT,
gender CHAR(1)


#### Port Dimensional Table - This data is from immigration_data.csv
port_id VARCHAR PRIMARY KEY, 
cicid INT,
port VARCHAR,
arrive_date INT,
mode VARCHAR,
departure_date INT,
visa VARCHAR

#### Temp Dimensional Table - This data is from GlobalLandTemperaturesByCity.csv
temp_id VARCHAR PRIMARY KEY, 
dt DATE,
avg_temp FLOAT,
avg_temp_uncer FLOAT,
city VARCHAR,
country VARCHAR,
latitude VARCHAR,
longitude VARCHAR

#### Demo Dimensional Table - This data is from us-cities-demographics.csv
demo_id SERIAL PRIMARY KEY,
city VARCHAR,
state VARCHAR,
male_pop INT,
female_pop INT,
tot_pop INT,
foreign_born INT,
race VARCHAR



