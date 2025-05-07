import sqlite3

def create_air_table():

    conn = sqlite3.connect('AirQuality.db')

    if conn:
        conn.execute('DROP TABLE IF EXISTS AirQuality')
        conn.execute('''
                        CREATE TABLE IF NOT EXISTS AirQuality (
                        id integer PRIMARY KEY,
                        PM1 integer NOT NULL,
                        PM2 integer NOT NULL,
                        PM3 integer NOT NULL,
                        DMY date NOT NULL,
                        Postcode text NOT NULL
                        )
                    ''')

    conn.close()


if __name__ == '__main__':
    create_air_table()