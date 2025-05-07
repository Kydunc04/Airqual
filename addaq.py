import sqlite3
import pandas as pd

def add_row(upm1, upm2, upm3, udmy, upostcode):

    conn = sqlite3.connect('AirQuality.db')
    cur = conn.cursor()

    cur.execute(f'''INSERT INTO AirQuality (pm1, pm2, pm3, dmy, postcode) 
    VALUES ('{upm1}', '{upm2}', {upm3}, '{udmy}', '{upostcode}')''')

    conn.commit()
    conn.close()
    return cur.rowcount


if __name__ == '__main__':
    m_list = []
    with open("example.csv") as f:
        next(f)

        # Data Cleaning
        for line in f:
            PM1, PM2, PM3, StrDate, Postcode = line.split(',')  # PM2 = PM2.5 & PM3 = PM10
            if PM1 and PM2 and PM3 and StrDate and Postcode != '':
                if PM1.isnumeric() and PM2.isnumeric() and PM3.isnumeric():
                    m_list.append([PM1, PM2, PM3, StrDate, Postcode[:-1]])

    mdb = pd.DataFrame(m_list)
    mdb = mdb.dropna()
    mdb.drop_duplicates(inplace=True)

    mdb = mdb.to_numpy()

    for row in mdb:
        PM1, PM2, PM3, StrDate, Postcode = row
        add_row(PM1, PM2, PM3, StrDate, Postcode)
