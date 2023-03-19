import telebot
import time
import random
from flask import Flask, request

'''secret = "87af8d5a-a870-415c-b719-6b2a3bfd9034"

bot = telebot.TeleBot('5775287129:AAFmi9Ds-N4OV8yv0yAlX-qT4hyG6DyPHUg')
bot.remove_webhook()
bot.set_webhook(url="https://BlazeStrix.pythonanywhere.com/{}".format(secret))

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

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

'''
import requests
from flask import Flask, request

app = Flask(__name__)

# Замените <TOKEN> на токен вашего Telegram бота
TOKEN = '5775287129:AAFmi9Ds-N4OV8yv0yAlX-qT4hyG6DyPHUg'

# Обработчик вебхука
@app.route('/{}'.format(TOKEN), methods=['POST'])
def webhook():
    # Получаем данные от Telegram
    update = request.get_json()

    # Проверяем, что данные не пусты
    if update:
        # Получаем ID чата и сообщение от пользователя
        chat_id = update['message']['chat']['id']
        message_text = update['message']['text']

        # Отправляем сообщение обратно пользователю
        send_message(chat_id, message_text)

    return 'OK'

# Функция для отправки сообщения пользователю
def send_message(chat_id, message_text):
    # Формируем запрос к API Telegram
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
    data = {'chat_id': chat_id, 'text': message_text}

    # Отправляем запрос
    response = requests.post(url, data=data)

    # Проверяем статус запроса
    if response.status_code != 200:
        print('Ошибка отправки сообщения:', response.status_code, response.text)

# Устанавливаем вебхук
def set_webhook():
    # Формируем запрос к API Telegram
    url = 'https://api.telegram.org/bot{}/setWebhook'.format(TOKEN)

    # Задаем URL вебхука
    # webhook_url = 'https://<your_server_url>/<TOKEN>'
    webhook_url = 'https://BlazeStrix.pythonanywhere.com/{}/5775287129:AAFmi9Ds-N4OV8yv0yAlX-qT4hyG6DyPHUg'
    # Формируем данные для запроса
    data = {'url': webhook_url}

    # Отправляем запрос
    response = requests.post(url, data=data)

    # Проверяем статус запроса
    if response.status_code != 200:
        print('Ошибка установки вебхука:', response.status_code, response.text)

if __name__ == '__main__':
    # Устанавливаем вебхук при запуске приложения
    set_webhook()

    # Запускаем приложение
    app.run()


# Запускаем бота
# bot.polling(none_stop=True, interval=0)

