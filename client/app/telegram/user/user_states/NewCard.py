

from telebot.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from app.telegram.bot import texts, bot
from app.telegram.user.User import UserState


class NewCard(UserState):
    _msg_id = None

    def send_menu(self) -> None:

        buttons = InlineKeyboardMarkup()

        buttons.add(
            InlineKeyboardButton(text="Зрозуміло", callback_data='exit ')
        )

        # TODO: send request to server to create cart

        response = True
        card = "1234 1234 1234 1234"
        pin = "1111"

        msg_text = texts.new_card.format(card, pin) if response else texts.card_limit
        new_msg = bot.send_message(self.user.tg_id, msg_text + "", reply_markup=buttons)

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
