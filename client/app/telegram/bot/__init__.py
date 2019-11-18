import os

from telebot import TeleBot


class Bot(TeleBot):

    def send_message(self, chat_id, text, disable_web_page_preview=None, reply_to_message_id=None, reply_markup=None,
                     parse_mode='HTML', disable_notification=None):
        return super().send_message(chat_id, text, disable_web_page_preview, reply_to_message_id, reply_markup,
                                    parse_mode, disable_notification)


bot = Bot(os.getenv('BOT_TOKEN'))

bot.set_webhook(os.getenv('NGROK_URL') + '/telegram/web_hook/')

from app.telegram.bot import handlers
