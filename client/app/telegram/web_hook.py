from telebot.types import Update
from flask import request, Response

from . import telegram
from .bot import bot


@telegram.route('/telegram/web_hook/', methods=['POST'])
def telegram_web_hook():

    """This route get new updates from Telegram server
    next this updates sends to handlers defined in handlers.py
    """

    update = Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])

    return Response('ok', 200)
