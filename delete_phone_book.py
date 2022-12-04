import sqlite3 as sql

global conn
global cursor

conn = sql.connect('data_numbers.db')
cursor = conn.cursor()

def delete_abonent():
    password = input('Введите пароль: ')

    if password != '123456':
       print('Пароль неверный')
       exit()
    else:
        phone_number_delete = input(f'Введите номер телефона абонента, данные о котором удаляются: ')
        cursor.execute(f"DELETE from phone_data where phone_number = {phone_number_delete}")
        conn.commit()

#delete_abonent()