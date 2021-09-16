""" 
Install library
    $ pip install python-dotenv
    $ pip install pyTelegramBotApi

To get Chat ID
    1. Create a channel
    2. Add your bot to channel
    3. Add @getidsbot
    4. Save chat-id

Run the script
    $ python telegram-bot.py
"""

import os
import telebot
import requests

# Load .env file data
from dotenv import load_dotenv

load_dotenv()

# Create telebot
API_KEY = os.getenv('API_KEY')
CHAT_ID = os.getenv('CHAT_ID')

bot = telebot.TeleBot(API_KEY, parse_mode='MARKDOWN')

# To reply the particular message
@bot.message_handler(commands=['Greet', 'greet'])
def greet(message):
    bot.reply_to(message, "Hey! how's it going")

# To send the message
@bot.message_handler(commands=['hello', 'hi', 'Hello', 'Hi'])
def hello(message):
    bot.send_message(message.chat.id, "Hello! How are you")

# To show all commands
@bot.message_handler(commands=['help'])
def help(message):
    msg = f"""
    Welcome commands
    /hello - Hello
    /Greet - Hey! how's it going
    """
    bot.send_message(message.chat.id, msg)

# To echo the message
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
 

bot.polling()
