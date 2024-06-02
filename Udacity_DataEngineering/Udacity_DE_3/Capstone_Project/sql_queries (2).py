# DROP TABLES

fact_table_drop = "DROP TABLE IF EXISTS fact_immi;"
people_table_drop = "DROP TABLE IF EXISTS people;"
port_table_drop = "DROP TABLE IF EXISTS port;"
demo_table_drop = "DROP TABLE IF EXISTS demo;"

# CREATE TABLES


fact_table_create = ("""
    CREATE TABLE IF NOT EXISTS fact_immi
    (
    fact_id SERIAL CONSTRAINT fact_key PRIMARY KEY, 
    cicid INT,
    state VARCHAR,
    country VARCHAR,
    year INT,
    month INT
    ) 
    ;""")


people_table_create = (""" 
    CREATE TABLE IF NOT EXISTS people 
    ( 
    people_id SERIAL CONSTRAINT people_key PRIMARY KEY, 
    cicid INT,
    citizen VARCHAR,
    resident VARCHAR,
    age INT,
    gender VARCHAR
    ) 
    ;""")


port_table_create = (""" 
    CREATE TABLE IF NOT EXISTS port 
    ( 
    port_id SERIAL CONSTRAINT port_key PRIMARY KEY, 
    cicid INT,
    port VARCHAR,
    arrive_date TIMESTAMP,
    mode VARCHAR,
    departure_date TIMESTAMP,
    visa VARCHAR
    ) 
    ;""")


demo_table_create = ("""
    CREATE TABLE IF NOT EXISTS demo
    (
    demo_id BIGSERIAL CONSTRAINT demo_key PRIMARY KEY,
    city VARCHAR,
    state VARCHAR,
    male_pop FLOAT,
    female_pop FLOAT,
    tot_pop FLOAT,
    foreign_born FLOAT,
    race VARCHAR
    )
    """)



# INSERT RECORDS

fact_table_insert = (""" 
    INSERT INTO fact_immi (fact_id, cicid, state, country, year, month)
    VALUES (DEFAULT, %s, %s, %s, %s, %s) 
    """)



people_table_insert = (""" 
    INSERT INTO people (people_id, cicid, citizen, resident, age, gender)  
    VALUES (DEFAULT, %s, %s, %s, %s, %s)  
    """)



port_table_insert = (""" 
    INSERT INTO port (port_id, cicid, port, arrive_date, mode, departure_date, visa) 
    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s) 
    ON CONFLICT (port_id)
    DO NOTHING
    """)



demo_table_insert = (""" 
    INSERT INTO demo (demo_id, city, state, male_pop, female_pop, tot_pop, foreign_born, race)
    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s) 
    """)


# QUERY LISTS

create_table_queries = [fact_table_create, people_table_create, port_table_create, demo_table_create]
drop_table_queries = [fact_table_drop, people_table_drop, port_table_drop, demo_table_drop]