from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from app.telegram.bot import bot, texts
from app.telegram.user.User import UserState
from app.telegram.user.user_states.CardMenu import CardMenu


class WaitPass(UserState):
    _msg_id = None

    def __init__(self):
        self._try_count = 0

    def send_menu(self) -> None:
        buttons = InlineKeyboardMarkup()

        buttons.add(
            InlineKeyboardButton(text="Назад", callback_data='back ')
        )

        self._msg_id = bot.send_message(self.user.tg_id, texts.wait_pin.format("**** **** **** " + self.user.cur_card[-4:]), reply_markup=buttons).message_id

    def handle_message_text(self, msg: Message) -> None:
        password = msg.text

        r = self.user.do_card_auth(password)

        bot.delete_message(self.user.tg_id, self._msg_id)

        if r.get("success", None):
            self.user.transition_to(CardMenu())
        else:
            self._try_count += 1
            if self._try_count < 3:
                buttons = InlineKeyboardMarkup()

                buttons.add(
                    InlineKeyboardButton(text="Назад", callback_data='back ')
                )

                self._msg_id = bot.send_message(self.user.tg_id, "Пароль не вірний спробуй ще раз...", reply_markup=buttons).message_id
            else:
                from app.telegram.user.user_states.OperationNotOk import OperationNotOk
                self.user.transition_to(OperationNotOk("To many bad auth requests."))

    def handle_button(self, call: CallbackQuery) -> None:
        expected_buttons = ["back"]

        cur_button, card_id = call.data.split(' ')
        if cur_button in expected_buttons:
            bot.delete_message(self.user.tg_id, call.message.message_id)
            if cur_button == "back":
                from app.telegram.user.user_states.StartMenu import StartMenu
                self.user.transition_to(StartMenu())

    def handle_command(self, msg: Message) -> None:
        pass
