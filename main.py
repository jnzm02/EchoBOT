import telebot
from decouple import config


API_KEY = config('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello, I am Echo bot")


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
