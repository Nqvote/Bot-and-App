import telebot
from telebot import types
from random import *
from datetime import datetime
import pytz

api_token='7248807888:AAE_m-iR4kFG8N9GrkSaeWWHJMX8J_V1Mn0'
bot=telebot.TeleBot(api_token)

def button_messsage():
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons=(["Время в МСК","Рандомное число","Твой ID"])
    markup.add(*buttons)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'привет бро. что хочешь?',reply_markup=button_messsage())

@bot.message_handler(content_types=['text'])
def handle_text(mes):
    if mes.text=='Время в МСК': 
        msc_time=datetime.now(pytz.timezone('Europe/Moscow'))
        bot.send_message(mes.chat.id, f"Текущее время в Москве: {msc_time.strftime('%H:%M:%S')}")
    elif mes.text == 'Рандомное число': bot.send_message(mes.chat.id, f'Случайное число: {randint(-100,100)}')
    elif mes.text == 'Твой ID': bot.send_message(mes.chat.id, mes.from_user.id)
    else: bot.send_message(mes.chat.id, 'Что ты имеешь в виду? Я не понимаю')

bot.infinity_polling()