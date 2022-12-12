#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2022 Maksim Perov <coder@frtk.ru>
#

import telebot
import requests
from time import sleep

TOKEN=''
GROUP_ID=''
TIMEOUT=60*10 # 10 minutes

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get(message):
    print(message.text)

while True:
    try:
        response = requests.get("https://pass.mipt.ru:2443", timeout=30)
    except:
        bot.send_message(GROUP_ID, "ALERT: pass.mipt.ru:2443 isn't available!")
    sleep(TIMEOUT)
