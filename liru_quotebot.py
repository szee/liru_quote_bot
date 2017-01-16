# coding: utf-8

"""
Бот отправляет случайную цитату из выбранного дневника на ли.ру
Есть всего две команды: "/rndquote" и "/help"
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import sys
import time
import datetime
import telepot


def handle(msg):
    chat_id = msg["chat"]["id"]
    command = msg["text"]
    print("Got command: {}".format(command))

#Обработка команды "/rndquote"
    if command == "/rndquote":
        url = "http://www.liveinternet.ru/users/893664"
        html = urlopen(url).read()
        raw = BeautifulSoup(html, "lxml")
        #В тегах <div class="GL_MAR10T GL_MAR10B MESS"> сидят посты
        text = raw.find_all("div", class_="GL_MAR10T GL_MAR10B MESS")
        clean_text = []

        for tx in text:
            #Бот посылает одно случайное предложение
            ls = re.split(r"\.(?!\d)", tx.get_text(strip=True).strip())
            clean_text = clean_text + ls
        bot.sendMessage(chat_id, random.choice(clean_text))
#Обработка команды "/help"
    elif command == "/help":
        bot.sendMessage(chat_id, 'Используйте "/rndquote", чтобы получить случайную цитату')


bot = telepot.Bot(sys.argv[1])
bot.message_loop(handle)

print("Listening...")

while 1:
    time.sleep(10)
