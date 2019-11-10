from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from app.telegram.bot import bot, texts
from app.telegram.models.User import UserState
from app.telegram.models.UserStates.CardMenu import CardMenu


class WaitPass(UserState):
    _msg_id = None

    def send_menu(self) -> None:
        buttons = InlineKeyboardMarkup()

        buttons.add(
            InlineKeyboardButton(text="Назад", callback_data='back ')
        )

        self._msg_id = bot.send_message(self.user.tg_id, "Введи пароль.", reply_markup=buttons).message_id

    def handle_message_text(self, msg: Message) -> None:
        password = msg.text

        # TODO: send request to server to check pass

        bot.delete_message(self.user.tg_id, self._msg_id)
        if password == '1111':
            self.user.transition_to(CardMenu())
        else:
            buttons = InlineKeyboardMarkup()

            buttons.add(
                InlineKeyboardButton(text="Назад", callback_data='back ')
            )

            self._msg_id = bot.send_message(self.user.tg_id, "Пароль не вірний спробуй ще раз...", reply_markup=buttons).message_id

    def handle_button(self, call: CallbackQuery) -> None:
        expected_buttons = ["back"]

        cur_button, card_id = call.data.split(' ')
        if cur_button in expected_buttons:
            bot.delete_message(self.user.tg_id, call.message.message_id)
            if cur_button == "back":
                from app.telegram.models.UserStates.StartMenu import StartMenu
                self.user.transition_to(StartMenu())

    def handle_command(self, msg: Message) -> None:
        pass
