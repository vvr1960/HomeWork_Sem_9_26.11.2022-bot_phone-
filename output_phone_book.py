import sqlite3 as sql

global conn
global cursor

conn = sql.connect('data_numbers.db')
cursor = conn.cursor()

def abonent_output():
    print('Введите фамилию абонента:\n')
    surname_output = input('Фамилия: ')
    print()
    
    cursor.execute(f"SELECT phone_number FROM phone_data WHERE (surname) = ('{surname_output}')")
    result = cursor.fetchall()
    if result == []:
        print('Данный абонент отсутствует в справочнике!')
    else:
        for row in result:
            print(f'Номер телефона: {row[0]}')
         
#abonent_output()