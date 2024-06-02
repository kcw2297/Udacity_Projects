import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour,weekofyear, date_format

config = configparser.ConfigParser() 
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config.get('AWS','AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY']=config.get('AWS','AWS_SECRET_ACCESS_KEY')


def create_spark_session():
    """
    Create spark session with necessary packages.
    """
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    """
    Process the song_data and make songs table and artists table.
    spark = spark session
    input_data = path to the file
    output_data = path to save the partition dataset
    """
    # get filepath to song data file
    song_data = os.path.join(input_data, "song_data/*/*/*/*.json")
    
    # read song data file
    df = spark.read.json(song_data, mode = "PERMISSIVE", columnNameOfCorruptRecord='corrupt_record').dropDuplicates().cache()

    # extract columns to create songs table
    songs_table = df.select(col("song_id"),col("title"),col("artist_id"),col("year"),col("duration"))
    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.partitionBy("year","artist_id").parquet(output_data+"/songs", mode="overwrite")

    # extract columns to create artists table
    artists_table = df.select(col("artist_id"),col("artist_name"),col("artist_location"),col("artist_latitude"),col("artist_longitude"))
    
    # write artists table to parquet files
    artists_table.write.parquet(output_data+"/artists", mode="overwrite")
    
    # create temporary table for songsplay table
    df.createOrReplaceTempView("song_df_table")

def process_log_data(spark, input_data, output_data):
    """
    Process the log_data and make songplays, users, and time table.
    input_data = path to the file
    output_data = path to save the partition dataset
    """
    # get filepath to log data file
    log_data =  os.path.join(input_data, "log_data/*.json")

    # read log data file
    df = spark.read.json(log_data).dropDuplicates()
    
    # filter by actions for song plays
    df =  df.filter(df.page == "NextSong").cache()

    # extract columns for users table    
    users_table = df.select(col("userId"),col("firstName"),col("lastName"),col("gender"),col("level")).distinct()
    
    # write users table to parquet files
    users_table.write.parquet(output_data+"/users", mode="overwrite")

    # create timestamp column from original timestamp column
    get_timestamp = udf(lambda x : datetime.fromtimestamp(x/1000), TimestampType())
    df = df.withColumn("timestamp", get_timestamp(col("ts")))
    
    # create datetime column from original timestamp column
    get_datetime = udf(lambda x : to_date(x), TimestampType())
    df = df.withColumn("start_time", get_datetime(col("ts")))
    
    # extract columns to create time table
    df = df.withColumn("hour", hour("timestamp"))
    df = df.withColumn("day", day("timestamp"))
    df = df.withColumn("week", weekofyear("timestamp"))
    df = df.withColumn("month", month("timestamp"))
    df = df.withColumn("year", year("timestamp"))
    df = df.withColumn("weekday", dayofweek("timestamp"))
    
    time_table = df.select(col("start_time"), col("hour"),col("day") \
                           ,col("week"),col("month"),col("year"),col("weekday")).distinct()
    
    # write time table to parquet files partitioned by year and month
    time_table.write.partitionBy("year","month").parquet(output_data+"/time", mode="overwrite")

    # read in song data to use for songplays table
    song_df = spark.sql("SELECT DISTINCT song_id, artist_id, artist_name FROM song_df_table")

    # extract columns from joined song and log datasets to create songplays table 
    songplays_table = df.join(song_df, song_df.artist_name == df.artist , "inner") \
                    .select(col("start_time"),col("userId"),col("level"),col("song_id") \
                            ,col("artist_id"),col("sessionId"),col("artist_location"),col("userAgent"))

    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.partitionBy("year","month") \
                        .parquet(output_data+"/songplays", mode="overwrite")


def main():
    """
    Process the functions.
    """
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://finaltest12"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()