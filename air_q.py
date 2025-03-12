from datetime import datetime
import pandas as pd

# There is an Enviro+ python module which could be useful

dt = datetime.now()

full_date = dt.strftime("%Y-%m-%d")
full_time = dt.strftime("%H:%M:%S")
full_day = dt.strftime("%A")
year = dt.year
month = dt.month
date = dt.day
hour = dt.hour

# Testing outputs - This would give the time the data is processed as
# opposed to the time the data was collected.
print(full_date)
print(full_time)
print(full_day)
print(type(full_date))
print(type(full_time))

# Created a simple example csv showing random PM1.0, PM2.5 & PM10
# numbers using Excel.

db = pd.read_csv('example.csv')
print(db.head(10))
# Info
print(db.info())
print(db.isna().sum())

# Fill NA's using Mean
x = db["PM2.5"].mean()
db["PM2.5"].fillna(x.round(), inplace=True)