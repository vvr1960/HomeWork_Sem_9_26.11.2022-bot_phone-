
from input_phone_book import data_input
from delete_phone_book import delete_abonent
from output_phone_book import abonent_output
from view_phone_book import data_view_csv_pandas
from correct_phone_book import correct_abonent

print()
print('МЕНЮ СПРАВОЧНИКА\n')
menu = input('Выберите, какое действие выполнить:\n "1" - Показать всё, "2" - Найти номер, "3"- Добавить абонента, "4" - Удалить абонента, "5" - Изменить данные\n')
if  menu == '1':
    data_view_csv_pandas()
elif menu == '2':
    abonent_output()
elif menu == '3':
    data_input()
elif menu == '4':
    delete_abonent()
elif menu == '5':
    correct_abonent()
else:
    print('Вы ввели неверный индекс меню!')    