""" 
Install library
    $ pip install python-dotenv
    $ pip install python-telegram-bot

Run the script
    $ python telegram_bot.py

To get chat-id
https://api.telegram.org/bot1<token>/sendMessage?chat_id=@channelName&text=123
"""
from telegram.ext import Updater, InlineQueryHandler, CommandHandler,  MessageHandler, Filters
from telegram.ext.dispatcher import run_async
import requests
import re
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

# @run_async
def bop(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def start(update, context):
    s = "Welcome I Am The Binance new coin Chat Bot! Your life has now changed forever."
    update.message.reply_text(s)
    context.bot.sendMessage(chat_id='@BinanceNewCoin', text='Some content')
    
def repeater(update, context):
    # if context.user_data[echo]:
    #     update.message.reply_text(update.message.text)
    update.message.reply_text(update.message.text)
    

def echo(update, context):
    command = context.args[0].lower()
    if("on" == command):
        context.user_data[echo] = True
        update.message.reply_text("Repeater Started")
    elif("off" == command):
        context.user_data[echo] = False
        update.message.reply_text("Repeater Stopped")

def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('echo', echo))
    dp.add_handler(MessageHandler(Filters.text, repeater))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()