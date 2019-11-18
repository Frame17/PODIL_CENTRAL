import json
import os

import requests
from telebot.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from app.telegram.bot import texts, bot
from app.telegram.user.User import UserState


class NewCard(UserState):
    _msg_id = None

    def __init__(self, call):
        self._call = call

    def send_menu(self) -> None:

        buttons = InlineKeyboardMarkup()

        buttons.add(
            InlineKeyboardButton(text="Зрозуміло", callback_data='exit ')
        )

        r = requests.get(os.getenv("SERVER_URL") + "generate-card?id=" + self.user.tg_id)

        res_dict = json.loads(r)

        if not res_dict.get("successful"):
            bot.answer_callback_query(callback_query_id=self._call.id, show_alert=True, text=res_dict["reason"])
            bot.send_message(self.user.tg_id, texts.card_limit.format(res_dict["reason"]), reply_markup=buttons)
        else:
            card = res_dict["id"]
            pin = res_dict["pin"]

            msg_text = texts.new_card.format(card, pin)
            bot.send_message(self.user.tg_id, msg_text, reply_markup=buttons)

    def handle_message_text(self, msg: Message) -> None:
        pass

    def handle_button(self, call: CallbackQuery) -> None:
        expected_buttons = ["ok", "exit"]

        cur_button, card_id = call.data.split(' ')
        if cur_button in expected_buttons:
            bot.delete_message(self.user.tg_id, call.message.message_id)
            if cur_button == "exit":
                from app.telegram.user.user_states.StartMenu import StartMenu
                self.user.transition_to(StartMenu())
