import numpy as np
from datetime import datetime
import pandas as pd
import requests

m_list = []
with open("example.csv") as f:
    next(f)

    for line in f:
        PM1, PM2, PM3, StrDate, Postcode = line.split(',')  #PM2 = PM2.5 & PM3 = PM10
        m_list.append([PM1, PM2, PM3, StrDate, Postcode[:-1]])

mdb = np.array(m_list)  # Changed to appending list when actual data must be inserted
print(f"{mdb}\n{'':=^33}\n")

# Data Cleaning
with open("mdb.csv", "a") as m:
    for l in mdb:
        PM1, PM2, PM3, Date, Post = l
        m.write(f"{PM1},{PM2},{PM3},{Date},{Post}\n")

# Last 7 days db
ls_list = []
dt = datetime(2025, 3, 13)  # This would become dt = datetime.now()
doy = int(dt.strftime("%j"))  # Day of the year out of 365

for row in mdb:
    y, m, d = row[3].split("-")
    row_date = datetime(int(y), int(m), int(d))
    if doy - 6 <= int(row_date.strftime("%j")) <= doy:
        ls_list.append(row)

print(f"{ls_list}\n{'':=^33}\n")
lsdf = pd.DataFrame(ls_list)
lsdf.to_csv("ls.csv", header=False, index=False)

# Last month db (30 days)
lm_list = []

for row in mdb:
    y, m, d = row[3].split("-")
    row_date = datetime(int(y), int(m), int(d))
    if doy - 29 <= int(row_date.strftime("%j")) <= doy:
        lm_list.append(row)

print(f"{lm_list}\n{'':=^33}\n")
lmdf = pd.DataFrame(lm_list)
lmdf.to_csv("lm.csv", header=False, index=False)

# If the date of collection cannot be listed from the raspberry pi python can
# timestamp each piece of data from when it is processed by the file rather by
# when it was collected.

# url = ""

# file = open('mdb.csv', 'rb')
# req = requests.post(url, files={"form tag thingy":file})

# print(req.text)