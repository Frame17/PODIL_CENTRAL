from telebot import TeleBot

from telebot.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    Message, CallbackQuery
)

from app.bot import texts


class PCBot(TeleBot):

    def change_state(self, tg_id: int, state: int, call: CallbackQuery = None) -> Message:
        """"""

        if call:
            self.delete_message(tg_id, call.message.message_id)

        buttons = InlineKeyboardMarkup()

        if state == 1:
            buttons.add(
                InlineKeyboardButton(
                    text=texts.add_card_button,
                    callback_data='add_card'
                ),
                InlineKeyboardButton(
                    text=texts.choose_card_button,
                    callback_data='choose_card'
                )
            )

        new_msg = self.send_message(tg_id, texts.state_1, reply_markup=buttons)

        return new_msg

    pass
