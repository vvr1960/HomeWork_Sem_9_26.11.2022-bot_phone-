import sqlite3 as sql

global conn
global cursor

conn = sql.connect('data_numbers.db')
cursor = conn.cursor()

def data_input():
    print('Введите данные абонента:\n')
    surname = input('Фамилия: ')
    name = input('Имя: ')
    patron = input('Отчество: ')
    phone_number = input('Номер телефона: ')

    pers_data = surname, name, patron, phone_number
    data_phone_list = """INSERT INTO phone_data (surname, name, patron, phone_number) values(?, ?, ?, ?);"""
    cursor.execute(data_phone_list, pers_data)
    conn.commit()

#data_input()
