# The telegram-bot

A telegram bot which send message, reply message etc.

## Create Bot from [@BotFather](https://telegram.me/botfather)
Follow the steps to create telegram bot
```
1. Message @BotFather to start the conversation
    /start
2. Create new bot
    /newbot
3. Choose a new name for your bot
    Telegram Tuts Bots
4. Choose a username, must end with 'bot', like 'TutsBot', 'tuts_bot'
    TeleTutsBot
5. On successfull creation, an API token will generate
6. Check you bot on - t.me/<username>
    t.me/TeleTutsBot
```


## To get Chat-id from [@GetIDs Bot](https://telegram.me/getidsbot)
```
1. Create another Group/Channel
2. Add your bot to Group/Channel
3. Add @getidsbot
4. Save chat-id
```


## 💻 Installation steps

1. Download the code
2. Create .env file and paste API_KEY
    ```
    # .env
    API_KEY="<API KEY from BOT FATHER>"
    CHAT_ID=<Chat id>
    ```
3. Install the library
    ```
    pip install python-dotenv
    pip install pyTelegramBotApi
    ```
4. Run the script 
    ```
    $ python py_telegram_bot_api.py
    $ python telegram_bot.py
    ```