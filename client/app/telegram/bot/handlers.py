import logging
from telebot.types import CallbackQuery, Message

from app.telegram.bot import bot
from app.telegram.models.UserStates.StartMenu import StartMenu
from app.telegram.models.User import User
from app.telegram.models.Users import Users

logger = logging.getLogger(__name__)

users = Users()


@bot.message_handler(commands=['start'])
def start_handler(msg: Message):
    """This handler runs when someone send '/start' to bot in Telegram"""

    logger.debug(msg)

    if users.get_user_by_tg_id(msg.from_user.id):
        return

    # TODO: send request to server

    user = User(msg.from_user.id, msg.from_user.first_name or '', msg.from_user.last_name or '', StartMenu())
    users.add_user(user)
    user.command_request(msg)


@bot.message_handler(regexp=r'^/+')
def command_handler(msg: Message):
    """"""

    logger.debug(msg)

    user = users.get_user_by_tg_id(msg.from_user.id)
    user.command_request(msg)


@bot.callback_query_handler(lambda call: True)
def button_handler(call: CallbackQuery):
    """"""

    logger.debug(call)

    user = users.get_user_by_tg_id(call.from_user.id)
    user.button_request(call)


@bot.message_handler(content_types=['text'])
def text_handler(msg: Message):
    """"""

    logger.debug(msg)

    user = users.get_user_by_tg_id(msg.from_user.id)
    user.message_text_request(msg)


