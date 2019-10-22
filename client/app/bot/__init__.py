import os
from flask import Blueprint

from .StateBot import StateBot

telegram = Blueprint('telegram', __name__)
bot = StateBot(os.getenv('BOT_TOKEN'))
bot.set_webhook(os.getenv('NGROK_URL') + '/telegram/web_hook/')

from . import routes, handlers
