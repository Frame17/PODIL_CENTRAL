import os
from flask import Blueprint

from .PCBot import PCBot

telegram = Blueprint('telegram', __name__)
bot = PCBot(os.getenv('BOT_TOKEN'))
bot.set_webhook(os.getenv('NGROK_URL') + '/telegram/web_hook/')

from . import routes, handlers
