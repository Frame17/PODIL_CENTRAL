import json
import os

import requests
from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from app.telegram.bot import texts, bot
from app.telegram.user.user_states.OperationNotOk import OperationNotOk
from app.telegram.user.user_states.WaitPass import WaitPass
from app.telegram.user.User import UserState


class ChooseCard(UserState):
    def send_menu(self) -> None:

        r = requests.get(os.getenv("SERVER_URL") + 'cards?id=' + str(self.user.tg_id))

        content = json.loads(r.content)

        try:
            cards = [str(x) for x in content["cards"]]
        except Exception as e:
            self.user.transition_to(OperationNotOk(content["reason"]))
            return

        buttons = InlineKeyboardMarkup()
        for card in cards:
            buttons.add(
                InlineKeyboardButton(text="**** **** **** " + card[-4:],
                                     callback_data='choose_card ' + card)
            )

        msg_text = 'Оберіть карту...' if len(cards) > 0 else texts.card_limit
        bot.send_message(self.user.tg_id, msg_text, reply_markup=buttons)

    def handle_message_text(self, msg: Message) -> None:
        pass

    def handle_button(self, call: CallbackQuery) -> None:
        expected_buttons = ["choose_card"]

        cur_button, card_id = call.data.split(' ')
        if cur_button in expected_buttons:
            bot.delete_message(self.user.tg_id, call.message.message_id)
            if cur_button == "choose_card":
                self.user.cur_card = card_id
                self.user.transition_to(WaitPass())

    def handle_command(self, msg: Message) -> None:
        pass
