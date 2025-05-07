import sqlite3
from datetime import datetime


def all_data():

    conn = sqlite3.connect('AirQuality.db')
    cur = conn.cursor()

    cur.execute('''SELECT * FROM AirQuality''')
    result = cur.fetchall()

    conn.close()
    return result


if __name__ == '__main__':
    with open("mdb.csv", "w") as m:
          for row in all_data():
            ID, PM1, PM2, PM3, Date, Postcode = row
            m.write(f"{PM1},{PM2},{PM3},{Date},{Postcode}\n")

    dt = datetime(2025, 3, 13)  # This would become dt = datetime.now()
    doy = int(dt.strftime("%j"))  # Day of the year out of 365

    with open("ls.csv", "w") as l:
        for row in all_data():
            ID, PM1, PM2, PM3, Date, Postcode = row
            y, m, d = Date.split("-")
            row_date = datetime(int(y), int(m), int(d))
            if doy - 6 <= int(row_date.strftime("%j")) <= doy:
                l.write(f"{PM1}, {PM2}, {PM3},{Date},{Postcode}\n")

    with open("lm.csv", "w") as lm:
        for row in all_data():
            ID, PM1, PM2, PM3, Date, Postcode = row
            y, m, d = Date.split("-")
            row_date = datetime(int(y), int(m), int(d))
            if doy - 29 <= int(row_date.strftime("%j")) <= doy:
                lm.write(f"{PM1}, {PM2}, {PM3},{Date},{Postcode}\n")