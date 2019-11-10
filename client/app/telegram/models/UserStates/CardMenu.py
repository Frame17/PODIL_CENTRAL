from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from app.telegram.bot import texts, bot
from app.telegram.models.User import UserState
from app.telegram.models.UserStates.Deposit import Deposit
from app.telegram.models.UserStates.Withdraw import Withdraw


class CardMenu(UserState):

    def send_menu(self) -> None:
        # TODO: request to server

        buttons = InlineKeyboardMarkup()

        buttons.add(
            InlineKeyboardButton(text="Зняти", callback_data='withdraw '),
            InlineKeyboardButton(text="Поповнити", callback_data='deposit '),
            # InlineKeyboardButton(text="Переслати", callback_data='transfer '),
            InlineKeyboardButton(text="Вийти", callback_data='exit ')
        )

        bot.send_message(self.user.tg_id, texts.card_menu.format("**** **** **** 1111", "200"), reply_markup=buttons)

    def handle_button(self, call: CallbackQuery) -> None:
        from app.telegram.models.UserStates.StartMenu import StartMenu
        expected_buttons = ["withdraw", "deposit", "transfer", "exit"]

        cur_button, card_id = call.data.split(' ')
        if cur_button in expected_buttons:
            bot.delete_message(self.user.tg_id, call.message.message_id)
            if cur_button == "withdraw":
                self.user.transition_to(Withdraw())
            elif cur_button == "deposit":
                self.user.transition_to(Deposit())
            # elif cur_button == "transfer":
            #     self.user.transition_to(Transfer())
            elif cur_button == "exit":
                self.user.transition_to(StartMenu())

    def handle_command(self, msg: Message) -> None:
        pass

    def handle_message_text(self, msg: Message) -> None:

        pass
