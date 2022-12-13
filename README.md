# telegramInformant
## Description

It helps to know what your remote resources are unavailable

## Docker startup

### Requirements

- [Docker](https://docs.docker.com/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

### How to start
1. Get project:
```console
$ git clone https://github.com/mperov/telegramInformant.git
$ cd telegramInformant/
```
2. 1) Change file `resources.json` that contains all remote hosts which will being checked;  
   2) [Create Telegram bot](https://t.me/BotFather);  
   3) Add token of your Telegram bot in `informant.py` by changing variable TOKEN and add recipient by modifiying GROUP_ID.  
3. Build and run container:
```console
$ docker-compose build
$ docker-compose up -d
```

**If it's all right you will receive greetings message from bot.**

## Typical startup

### Requirements
At first I recommend to create special Python virtual enviroment by
```console
$ sudo apt-get install python3-venv -y
$ python3 -m venv telegramInformant
$ source telegramInformant/bin/activate
```

Next install some Python modules - `pip3 install -r requirements` or `python3 -m pip install -r requirements`  
If you don't have pip3 then you may install it [how described here](https://pip.pypa.io/en/stable/installation/)

### Usage

The first change file `resources.json` that contains all remote hosts which will being checked.  
The second Add token of your Telegram bot in `informant.py` by changing variable TOKEN and add recipient by modifiying GROUP_ID.  
Finally
```console
$ source telegramInformant/bin/activate
$ ./informant.py
```
