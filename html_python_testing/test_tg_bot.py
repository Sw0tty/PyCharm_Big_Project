import telebot
import random

TOKEN = '5925041262:AAHAUWj1bBbOkPFHKZRffGxA-lQZYg1KvBE'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help', 'calculate'])  # Распознование команд
def handler_start_stop(message: telebot.types.Message):
    if message.text == '/start':
        bot.reply_to(message, f"Это моя команда: {message.text}")
    elif message.text == '/help':
        bot.reply_to(message, f"Это моя команда: {message.text}")
    elif message.text == '/calculate':
        bot.reply_to(message, f"Сколько будет {random.randint(0, 100)} + {random.randint(0, 100)}?")


@bot.message_handler(content_types=['text'])  # Распознование текстового сообщения
def function_name(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username}")


@bot.message_handler(content_types=['voice'])  # Распознование голосового сообщения
def function_name(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Если бы я мог говорить, я бы ответил,"
                                      f"{message.chat.first_name} {message.chat.last_name}")


@bot.message_handler(content_types=['photo'])  # Распознование фотографий
def function_name(message: telebot.types.Message):
    bot.reply_to(message, f"Nice meme XDD")


bot.polling(none_stop=True)
