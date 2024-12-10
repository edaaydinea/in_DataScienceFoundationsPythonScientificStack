# What is the mean speed (mile/hour) in taxi.parquet?

# - Run download_data.py to download the data

# - Load the data using pandas
import pandas as pd

df = pd.read_parquet('./taxi.parquet')

# mean speed (mile/hour)
mask = df["tpep_dropoff_datetime"] > df["tpep_pickup_datetime"]
df = df[mask]

times = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
times_hour = times / pd.Timedelta(1, "hour")
speed = df["trip_distance"] / times_hour

print(speed.mean())