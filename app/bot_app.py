# -*- encoding: utf8 -*-
import telegram
from flask import Flask, request
import random
import config

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True
DEBUG = True

bot = telegram.Bot(token=config.token)

list = config.list

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook(config.url)
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
        
      
@app.route('/HOOK', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = random.choice(list)

        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'