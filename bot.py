import config
from view_phone_book import data_view_csv_pandas
from output_phone_book import abonent_output
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
import logging

 
ABONENT_PHONE = "abonents"
PHONE_BOOK = "all"

def generat_keyboard():
    keyboard = [
        [InlineKeyboardButton("Номер абонента", callback_data=ABONENT_PHONE),
         InlineKeyboardButton("Весь справочник", callback_data=PHONE_BOOK)]    
    ]          

    return InlineKeyboardMarkup(keyboard)

def keyboard_requlate(update: Update, context):
    query = update.callback_query
    current_callbacks = query.data    

    chat_id1 = update.effective_message.chat_id

    query.edit_message_text(
        text=update.effective_message.text
    )

    if current_callbacks == ABONENT_PHONE:
        context.bot.send_message(
            chat_id = chat_id1,
            text = 'Введите фамилию абонента'
        )
                
    elif current_callbacks == PHONE_BOOK:
        context.bot.send_message(
            chat_id = chat_id1,
            text = f'{data_view_csv_pandas()}'
        )


def hello(update: Update, context):
    context.bot.send_message(
        chat_id = update.effective_message.chat_id,
        text = update.effective_message.text
    )

def start(update: Update, context):
    user_name = update.effective_user.first_name
    context.bot.send_message(
        chat_id = update.effective_message.chat_id,
        text = f'Привет, {user_name}!\nДобро пожаловать в самый новый телефонный справочник!\nВыберите из меню внизу, что желаете посмотреть',
        reply_markup = generat_keyboard()
    )    

def main():
    my_update = Updater(token = config.TOKEN, use_context=True)

    keyboard_handler = CallbackQueryHandler(callback=keyboard_requlate, pass_chat_data=True)
    my_handler = MessageHandler(Filters.all, hello)
    start_handler = CommandHandler("start", start)

    my_update.dispatcher.add_handler(keyboard_handler)
    my_update.dispatcher.add_handler(start_handler)
    my_handler = MessageHandler(Filters.all, hello)
    my_update.dispatcher.add_handler(my_handler)


    my_update.start_polling()
    my_update.idle()



if __name__ == "__main__":
    main()









# import telebot
# from telebot import types

# bot = telebot.TeleBot('5691621564:AAF7vLrEImD_fRbxAGs_UYLnskjQIwV4yLY')

# name = ''
# surname = ''
# age = 0
# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/reg':
#         bot.send_message(message.from_user.id, "Как тебя зовут?")
#         bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
#     else:
#         bot.send_message(message.from_user.id, 'Напиши /reg')

# def get_name(message): #получаем фамилию
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
#     bot.register_next_step_handler(message, get_surname)

# def get_surname(message):
#     global surname
#     surname = message.text
#     bot.send_message('Сколько тебе лет?')
#     bot.register_next_step_handler(message, get_age)

# def get_age(message):
#     global age
#     while age == 0: #проверяем что возраст изменился
#         try:
#              age = int(message.text) #проверяем, что возраст введен корректно
#         except Exception:
#              bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
#              bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')

# def get_age(message):
#     global age
#     while age == 0: #проверяем что возраст изменился
#         try:
#              age = int(message.text) #проверяем, что возраст введен корректно
#         except Exception:
#              bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
#     keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
#     key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
#     keyboard.add(key_yes); #добавляем кнопку в клавиатуру
#     key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
#     keyboard.add(key_no)
#     question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
#     bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
#         ... #код сохранения данных, или их обработки
#         bot.send_message(call.message.chat.id, 'Запомню : )')
#     elif call.data == "no":
#          ... #переспрашиваем

# bot.polling(none_stop=True, interval=0)