from telebot.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from app.telegram.bot import texts, bot
from app.telegram.user.user_states.ChooseCard import ChooseCard
from app.telegram.user.User import UserState


class StartMenu(UserState):
    _buttons = ["create_card", "my_cards"]

    def send_menu(self) -> None:
        self.user.cur_card = None
        msg_text = texts.start_message

        buttons = InlineKeyboardMarkup()

        buttons.add(
            InlineKeyboardButton(text="Створити карту", callback_data='create_card '),
            InlineKeyboardButton(text="Мої карти", callback_data='my_cards ')
        )

        bot.send_message(self.user.tg_id, msg_text, reply_markup=buttons)

    def handle_button(self, call: CallbackQuery) -> None:

        cur_button = call.data.split(' ')[0]
        if cur_button in self._buttons:
            bot.delete_message(self.user.tg_id, call.message.message_id)
            if cur_button == "create_card":
                from app.telegram.user.user_states.NewCard import NewCard
                self.user.transition_to(NewCard(call))

            elif cur_button == "my_cards":
                self.user.transition_to(ChooseCard())

    def handle_message_text(self, msg: Message) -> None:
        pass
