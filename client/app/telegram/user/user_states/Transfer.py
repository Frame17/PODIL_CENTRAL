from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from app.telegram.bot import bot, texts
from app.telegram.user.User import UserState


class Transfer(UserState):
    _msg_id = None
    _amount = None

    def send_menu(self) -> None:
        r = self.user.get_balance()
        buttons = InlineKeyboardMarkup()

        buttons.add(
            InlineKeyboardButton(text="Назад", callback_data='back ')
        )

        self._msg_id = bot.send_message(self.user.tg_id,
                                        texts.transfer_1.format(r["balance"]), reply_markup=buttons).message_id

    def handle_button(self, call: CallbackQuery) -> None:
        expected_buttons = ["back"]

        cur_button, card_id = call.data.split(' ')
        if cur_button in expected_buttons:
            bot.delete_message(self.user.tg_id, call.message.message_id)
            if cur_button == "back":
                from app.telegram.user.user_states.CardMenu import CardMenu
                self.user.transition_to(CardMenu())

    def handle_message_text(self, msg: Message) -> None:
        if not self._amount:
            bot.delete_message(self.user.tg_id, self._msg_id)
            try:
                amount = int(msg.text)

                if int(self.user.get_balance()["balance"]) - amount < 0:
                    from app.telegram.user.user_states.OperationNotOk import OperationNotOk
                    self.user.transition_to(OperationNotOk("Low balance!"))
                self._amount = amount
                buttons = InlineKeyboardMarkup()
                buttons.add(
                    InlineKeyboardButton(text="Назад", callback_data='back ')
                )

                self._msg_id = bot.send_message(self.user.tg_id, texts.transfer_2, reply_markup=buttons).message_id
            except ValueError:
                buttons = InlineKeyboardMarkup()
                buttons.add(InlineKeyboardButton(text="Назад", callback_data='back '))
                self._msg_id = bot.send_message(self.user.tg_id,
                                                "Це не число, спробуй ще раз...", reply_markup=buttons).message_id
        else:
            to_card = msg.text

            self.user.do_transfer(self._amount, to_card)

