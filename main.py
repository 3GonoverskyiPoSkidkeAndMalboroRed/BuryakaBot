import telebot
from telebot import types

# Инициализация бота с токеном
bot = telebot.TeleBot("6673408905:AAFZs3MYjiKTrtXIUEKOUdwL0Q92WGH5t8g")

# Глобальные переменные для хранения данных пользователя
name = ''
surname = ''
age = 0

# Обработчик команды /reg
@bot.message_handler(commands=['reg'])
def start(message):
    bot.send_message(message.from_user.id, "Как тебя зовут?")
    bot.register_next_step_handler(message, get_name)

# Функция для получения имени
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname)

# Функция для получения фамилии
def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько тебе лет?")
    bot.register_next_step_handler(message, get_age)

# Функция для получения возраста
def get_age(message):
    global age
    try:
        age = int(message.text)
        bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_yes, key_no)
        bot.send_message(message.from_user.id, text='Подтвердите информацию:', reply_markup=keyboard)
    except ValueError:
        bot.send_message(message.from_user.id, "Цифрами, пожалуйста.")
        bot.register_next_step_handler(message, get_age)

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def final(call):
    if call.data == "yes":
        bot.send_message(call.from_user.id, 'Запомню : )')
    elif call.data == "no":
        bot.send_message(call.from_user.id, 'Давай попробуем еще раз. Напиши /reg')

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)