from telebot.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from app.telegram.bot import texts, bot
from app.telegram.models.User import UserState


class OperationNotOk(UserState):
    _msg_id = None

    def send_menu(self) -> None:
        buttons = InlineKeyboardMarkup()

        buttons.add(
            InlineKeyboardButton(text="Меню картки", callback_data='ok '),
            InlineKeyboardButton(text="Завершити", callback_data='exit ')
        )

        self._msg_id = bot.send_message(self.user.tg_id, texts.operation_not_ok.format("Low Balance"), reply_markup=buttons).message_id

    def handle_message_text(self, msg: Message) -> None:
        pass

    def handle_button(self, call: CallbackQuery) -> None:
        expected_buttons = ["ok", "exit"]

        cur_button, card_id = call.data.split(' ')
        if cur_button in expected_buttons:
            bot.delete_message(self.user.tg_id, call.message.message_id)
            if cur_button == "ok":
                from app.telegram.models.UserStates.CardMenu import CardMenu
                self.user.transition_to(CardMenu())
            if cur_button == "exit":
                from app.telegram.models.UserStates.StartMenu import StartMenu
                self.user.transition_to(StartMenu())

    def handle_command(self, msg: Message) -> None:
        pass
