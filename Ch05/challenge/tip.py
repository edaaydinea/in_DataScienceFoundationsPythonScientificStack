"""
- Load the taxi data.
- Remove all rows with either total_amount <= 0 or
  passenger_count == 0
- Create a bar chart of average tip % per passenger_count
- Create a bar chart of average tip % per day of week
"""

# Load the taxi data.
import pandas as pd
from calendar import day_abbr
import matplotlib.pyplot as plt

time_cols = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]

df = pd.read_csv('../data/taxi.csv', parse_dates=time_cols)

vendors = {1: 'Creative', 2: 'VeriFone'}

df['Vendor'] = df['VendorID'].map(vendors).astype('category')

# Remove all rows with either total_amount <= 0 or passenger_count == 0
df = df[(df['total_amount'] > 0) & (df['passenger_count'] > 0)]

df['tip_pct'] = df['tip_amount'] / df['total_amount'] * 100

# Create a bar chart of average tip % per passenger_count
by_count = df.groupby('passenger_count')['tip_pct'].mean()
ax = by_count.plot.bar(title='Tip % by Passenger Count', rot=0)
ax.set_ylabel('Tip %')
ax.set_xlabel('Passenger Count')
plt.show()

# Create a bar chart of average tip % per day of week
day_of_week = df['tpep_pickup_datetime'].dt.weekday
by_day = df.groupby(day_of_week)['tip_pct'].mean()
by_day.index = [day_abbr[i] for i in by_day.index]
ax = by_day.plot.bar(title='Tip % by Day of Week', rot=0)
ax.set_ylabel('Tip %')
ax.set_xlabel('Day of Week')
plt.show()

