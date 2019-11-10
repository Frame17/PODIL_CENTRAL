from telebot.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from app.telegram.bot import texts, bot
from app.telegram.user.User import UserState


class Withdraw(UserState):
    _msg_id = None

    def send_menu(self) -> None:

        r = self.user.get_balance()

        buttons = InlineKeyboardMarkup()

        buttons.add(
            InlineKeyboardButton(text="Назад", callback_data='back ')
        )

        self._msg_id = bot.send_message(self.user.tg_id, texts.withdraw.format(r["balance"]),
                                        reply_markup=buttons).message_id

    def handle_message_text(self, msg: Message) -> None:
        bot.delete_message(self.user.tg_id, self._msg_id)
        try:
            amount = int(msg.text)

            r = self.user.do_withdraw(amount)

            if r.get("successful", None):
                from app.telegram.user.user_states.OperationOk import OperationOk
                self.user.transition_to(OperationOk("withdraw"))
            elif r.get("successful", None) == False:
                from app.telegram.user.user_states.OperationNotOk import OperationNotOk
                self.user.transition_to(OperationNotOk(r["reason"]))
            else:
                from app.telegram.user.user_states.OperationNotOk import OperationNotOk
                self.user.transition_to(OperationNotOk("Hvatit balovacca!"))
        except ValueError as e:
            print(e)
            buttons = InlineKeyboardMarkup()

            buttons.add(
                InlineKeyboardButton(text="Назад", callback_data='back ')
            )
            self._msg_id = bot.send_message(self.user.tg_id, "Це не число, спробуй ще раз...",
                                            reply_markup=buttons).message_id

    def handle_button(self, call: CallbackQuery) -> None:
        expected_buttons = ["back"]

        cur_button, card_id = call.data.split(' ')
        if cur_button in expected_buttons:
            bot.delete_message(self.user.tg_id, call.message.message_id)
            if cur_button == "back":
                from app.telegram.user.user_states.CardMenu import CardMenu
                self.user.transition_to(CardMenu())

    def handle_command(self, msg: Message) -> None:
        pass
