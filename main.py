import aiogram
from aiogram.types import message
from aiogram.utils import executor
from pip._internal.cli.cmdoptions import python

from telebot import types
import telebot
bot = telebot.TeleBot("6673408905:AAFZs3MYjiKTrtXIUEKOUdwL0Q92WGH5t8g")
PROXY_URL = "http://10.136.2.7:3128"api_hash = "4200ac0d2ea54533d272fb72f553e3b7"api_id = "25840274"#@bot.message_handler(content_types=['text', 'document', 'audio'])name = ''surname = ''age = 0@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Напиши /reg")

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько тебе лет?")
    bot.register_next_step_handler(message, get_age)
# 57  44 strdef get_age(message):
    global age

    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Цифрами, пожалуйста.")
            bot.send_message(message.from_user.id, "Еще раз, сколько тебе лет?")
            bot.register_next_step_handler(message, get_age)
            break    else:
        bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')
        bot.register_next_step_handler(message, final)

#def get_age(message):#    global age#    while age == 0:#        try:#            age = int(message.text)#       except Exception:#            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')#            keyboard = types.InlineKeyboardMarkup()#            key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')#            keyboard.add(key_yes)#            key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')#            keyboard.add(key_no)#            question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'#            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)#@bot.callback_query_handler(func=lambda call: True)def final(message):
    if message.text == "yes":
        bot.send_message(message.from_user.id, 'Запомню : )')
    elif message.text == "no":
        ...
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
