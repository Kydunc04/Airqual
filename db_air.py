import numpy as np
from datetime import datetime

m_list = []
with open("example.csv") as f:
    next(f)

    for line in f:
        PM1, PM2, PM3, StrDate = line.split(',')  #PM2 = PM2.5 & PM3 = PM10
        m_list.append([PM1, PM2, PM3, StrDate[:-1]])

mdb = np.array(m_list)
print(f"{mdb}\n{'':=^33}\n")

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


# If the date of collection cannot be listed from the raspberry pi python can
# timestamp each piece of data from when it is processed by the file rather by
# when it was collected.