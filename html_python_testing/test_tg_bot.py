import telebot
import random
from tg_bot_numbers_str import NumberStr
from morse_code import Morse
from os import getenv
from dotenv import load_dotenv


load_dotenv()
TOKEN = getenv('TOKEN')


# TOKEN = 'in my tg name=echo_boy'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help_beta'])
def help_beta(message):
    bot.send_message(message.chat.id, "Данная функция имеет БЕТА статус")


@bot.message_handler(commands=['start', 'help', 'calculate'])  # Распознавание команд
def handler_start_stop(message):
    if 'start' in message.text:
        bot.reply_to(message, f"Это моя команда: {message.text}")
    elif message.text == '/help':
        bot.reply_to(message, f"Это моя команда: {message.text}")
    elif message.text == '/calculate':
        bot.reply_to(message, f"Сколько будет {random.randint(0, 100)} + {random.randint(0, 100)}?")


# @bot.message_handler(content_types=['text'])  # Распознавание текстового сообщения
# def function_name(message: telebot.types.Message):
#     input_str = NumberStr.transform_string_to_integer(message.text)
#     bot.send_message(message.chat.id, f"Это число: {input_str}")


@bot.message_handler(commands=['is_number'])
def is_number(message):
    bot.reply_to(message, "Хорошо, какое число угадать?")

    bot.register_next_step_handler(message, transform_string_to_integer)

    # input_str = NumberStr.transform_string_to_integer(message.text)
    # if input_str.lower() == 'хватит':
    #     bot.reply_to(message, "Захотите поиграть, пишите")


def transform_string_to_integer(message):
    s = message.text
    s = s.lower().split()
    basic_dict = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,
                  'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'двенадцать': 12, 'сорок': 40,
                  'девяносто': 90, 'сто': 100, 'двести': 200, 'тысяча': 1000, 'миллион': 1000000}
    num_from_str = []
    for num in s:
        # print(num)
        if num in basic_dict and len(s) == 1:
            return bot.send_message(message.chat.id, f"Это число: {basic_dict[num]}")
        elif num in basic_dict:
            num_from_str.append(basic_dict[num])
        else:
            for i in basic_dict.keys():
                if i in num or i[:-1] in num:
                    # print(i)
                    # if i == num or i[:-1] == num:
                    #     num_from_str.append(basic_dict[i])
                    if i + 'адцать' == num:
                        num_from_str.append(int('1' + str(basic_dict[i])))
                    elif i + 'надцать' == num or i[:-1] + 'надцать' == num:
                        num_from_str.append(int('1' + str(basic_dict[i])))
                    elif i + 'дцать' == num:
                        num_from_str.append(int(str(basic_dict[i]) + '0'))
                    elif i + 'десят' == num:
                        num_from_str.append(int(str(basic_dict[i]) + '0'))
                    elif i + 'ста' == num or i + 'сот' == num or i[:-1] + 'сти' == num:
                        num_from_str.append(int(str(basic_dict[i]) + '00'))

    # return num_from_str
    if not num_from_str:
        return "Неизвестное число"
    elif len(num_from_str) <= 3:
        return bot.send_message(message.chat.id, f"Это число: {sum(num_from_str)}")
    elif len(num_from_str) == 4:
        return bot.send_message(message.chat.id, f"Это число: {num_from_str[0] + sum(num_from_str)}")
    elif len(num_from_str) > 4:
        print(num_from_str)
        return bot.send_message(message.chat.id, f"Это число: {sum(num_from_str)}")

# @bot.message_handler(func=lambda message: message.text.lower() == "число")
# def function_name(message: telebot.types.Message):
#     bot.reply_to(message, "Хорошо, какое число угадать?")
#     while True:
#         input_str = NumberStr.transform_string_to_integer(message.text)
#         if input_str == 'хватит':
#             bot.reply_to(message, "Захотите поиграть, пишите")
#             break
#         bot.send_message(message.chat.id, f"Это число: {input_str}")



@bot.message_handler(content_types=['voice'])  # Распознавание голосового сообщения
def function_name(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Если бы я мог говорить, я бы ответил,"
                                      f"{message.chat.first_name} {message.chat.last_name}")


@bot.message_handler(content_types=['photo'])  # Распознавание фотографий
def function_name(message: telebot.types.Message):
    bot.reply_to(message, f"Nice meme XDD")


bot.polling(none_stop=True)
