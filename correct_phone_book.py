
import sqlite3 as sql

global conn
global cursor

conn = sql.connect('data_numbers.db')
cursor = conn.cursor()

def correct_abonent():
    password = input('Введите пароль: ')

    if password != '123456':
       print('Пароль неверный')
       exit()
    else:
        info_abonent_correct = input(f'Введите фамилю абонента, данные о котором корректируются: \n')
        column_correct = input(f'Введите наименование столбца, в который надо внести изменение (surname, name, patron, phone_number):\n')
        data_correct = input('Введите откорректированные данные: \n')
        cursor.execute(f"UPDATE phone_data SET {column_correct} = '{data_correct}' WHERE surname = '{info_abonent_correct}'")
        conn.commit()

#correct_abonent()


