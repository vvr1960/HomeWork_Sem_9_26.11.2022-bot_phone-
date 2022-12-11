import csv
import sqlite3 as sql
import pandas as pd

def data_view_csv_pandas():
    conn = sql.connect('data_numbers.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phone_data")
    conn.commit()

    row_csv_arr = []
    for row in cursor:
        row_csv = list(row)
        row_csv_arr.append(row_csv)
        
    with open("data_numbers.csv", mode="w", newline = '', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Фамилия", "Имя", "Отчество", "Номер_телефона"])
        file_writer.writerows(sorted(row_csv_arr, key=lambda x: x[0]))
    df = pd.read_csv('data_numbers.csv')
    print(df)
    return df
     
#data_view_csv_pandas()