import logging
from telebot.types import CallbackQuery, Message

from . import bot
from . import texts

logger = logging.getLogger(__name__)


@bot.message_handler(commands=['start'])
def start_handler(msg: Message):

    """This handler runs when someone send '/start' to bot in Telegram"""

    logger.debug(msg)

    tg_id = msg.from_user.id
    f_name = msg.from_user.first_name or ''
    l_name = msg.from_user.last_name or ''

    logger.debug(f'START HANDLER id:{tg_id} name:{f_name} {l_name}')

    # TODO: send request to server (check may be this user is already exist)

    msg_text = texts.start_message
    bot.change_state(tg_id, state=1, header_text=msg_text)


def button_handler(call: CallbackQuery, buttons: list) -> bool:
    try:
        button_name = call.data.split(' ')[0]
        return button_name in buttons
    except Exception as e:
        logger.error(e)
        return False


@bot.callback_query_handler(lambda call: button_handler(call, buttons=['create_card']))
def create_card(call: CallbackQuery):
    """"""

    logger.debug(call)

    tg_id = call.from_user.id

    # TODO: send request to server to create cart

    response = True
    card = "1234 1234 1234 1234"

    msg_text = texts.new_card.format(card) if response else texts.card_limit
    bot.change_state(tg_id, state=1, header_text=msg_text, call=call)


@bot.callback_query_handler(lambda call: button_handler(call, buttons=['choose_card']))
def create_card(call: CallbackQuery):
    """"""

    logger.debug(call)

    tg_id = call.from_user.id

    # TODO: send request to server to create cart

    response = ["1234 1234 1234 1234", "1234 1234 1234 5555", "1234 1234 1234 6545"]
    card = "1234 1234 1234 1234"

    msg_text = texts.new_card.format(card) if response else texts.card_limit
    bot.change_state(tg_id, state=1, header_text=msg_text, call=call)




