import logging

from . import bot
from . import texts

logger = logging.getLogger(__name__)


@bot.message_handler(commands=['start'])
def start_handler(msg):

    """This handler runs when someone send '/start' to bot in Telegram"""

    logger.info(msg)

    tg_id = msg.from_user.id
    f_name = msg.from_user.first_name or ''
    l_name = msg.from_user.last_name or ''

    logger.info(f'START id:{tg_id} name:{f_name} {l_name}')

    # TODO: send request to server

    bot.send_message(tg_id, texts.start_message)
    bot.change_state(tg_id, 1)
