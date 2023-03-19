import telebot
import time
import random

bot = telebot.TeleBot('5775287129:AAFmi9Ds-N4OV8yv0yAlX-qT4hyG6DyPHUg')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, 'Теперь я буду писать тебе комплименты')
    while True:
        data = open("data_base.txt", "r")
        lines = data.readlines()
        n = random.randint(0, 43200)
        time.sleep(86400 - n)
        # time.sleep(1)
        # c = random.choice(lines)
        # print(c)
        bot.send_message(message.chat.id, random.choice(lines))


# Запускаем бота
bot.polling(none_stop=True, interval=0)

