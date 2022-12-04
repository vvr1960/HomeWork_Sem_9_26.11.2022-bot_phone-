
import sqlite3 as sql


conn = sql.connect('data_numbers.db')
cursor = conn.cursor()


cursor.execute("""CREATE TABLE phone_data(
                   surname TEXT,
                   name TEXT,
                   patron TEXT,
                   phone_number INTEGER);
                   """)
conn.commit()
cursor.close()



