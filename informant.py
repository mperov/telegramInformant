#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2023 Maksim Perov <coder@frtk.ru>
#

import telebot
import requests
import socket
import json
from time import sleep

TOKEN=''
GROUP_ID=''
GLOBAL_TIMEOUT=60*10 # 10 minutes
CONNECT_TIMEOUT=3
ATTEMTS=5

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get(message):
    print(message.text)

def opened(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

def check_host(ip, port):
    ipup = False
    for i in range(ATTEMTS):
        if opened(ip, port):
            ipup = True
            break
        else:
            sleep(CONNECT_TIMEOUT)
    return ipup

def alert(hostname, _socket, available = False, hidden = False):
    if not available:
        postfix = " ) isn't available!"
        if hidden:
            postfix += "\nIt is okay, because resource should be unavailable."
    else:
        postfix = " ) is available!"
        if hidden:
            postfix += "\nAHTUNG, because resource should be unavailable!!!"
    bot.send_message(GROUP_ID, "ALERT: " + hostname + "( " + _socket + postfix)

def routine(resources):
    for hostname in resources:
        res = resources[hostname]
        hidden = False
        if not 'available' in res:
            value = True
            if 'hidden' in res:
                if res['hidden'] == "yes":
                    value = False
                    hidden = True
            res.update({'available' : value})
        _socket = res['host'] + ":" + res['port']
        if res['type'] in ['https', 'http']:
            try:
                response = requests.get(res['type'] + "://" + _socket, timeout=30)
                if not res['available']:
                    alert(hostname, _socket, True, hidden)
                    res['available'] = True
            except:
                if res['available']:
                    alert(hostname, res['type'] + "://" + _socket, False, hidden)
                    res['available'] = False
        else:
            if not check_host(res['host'], res['port']):
                if res['available']:
                    alert(hostname, _socket, False, hidden)
                    res['available'] = False
            elif not res['available']:
                alert(hostname, _socket, True, hidden)
                res['available'] = True

if __name__ == "__main__":
    resources = {}
    try:
        with open("resources.json", "r") as file:
            resources = json.load(file)
    except:
        print("Input data error!")
        exit(-1)
    if resources != {}:
        bot.send_message(GROUP_ID, "Hello! I'm Telegram bot! It's my first running! I'll notify you about hosts availability!")
        while True:
            routine(resources)
            sleep(GLOBAL_TIMEOUT)
