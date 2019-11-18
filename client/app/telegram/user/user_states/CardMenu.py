from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from app.telegram.bot import texts, bot
from app.telegram.user.User import UserState
from app.telegram.user.user_states.Deposit import Deposit
from app.telegram.user.user_states.Transfer import Transfer
from app.telegram.user.user_states.Withdraw import Withdraw


class CardMenu(UserState):

    def send_menu(self) -> None:
        r = self.user.get_balance()

        buttons = InlineKeyboardMarkup()

        buttons.add(
            InlineKeyboardButton(text="Зняти", callback_data='withdraw '),
            InlineKeyboardButton(text="Поповнити", callback_data='deposit '),
            InlineKeyboardButton(text="Переслати", callback_data='transfer '),
            InlineKeyboardButton(text="Вийти", callback_data='exit ')
        )

        bot.send_message(self.user.tg_id,
                         texts.card_menu.format("**** **** **** " + self.user.cur_card[-4:], r["balance"]),
                         reply_markup=buttons)

    def handle_button(self, call: CallbackQuery) -> None:
        from app.telegram.user.user_states.StartMenu import StartMenu
        expected_buttons = ["withdraw", "deposit", "transfer", "exit"]

        cur_button, card_id = call.data.split(' ')
        if cur_button in expected_buttons:
            bot.delete_message(self.user.tg_id, call.message.message_id)
            if cur_button == "withdraw":
                self.user.transition_to(Withdraw())
            elif cur_button == "deposit":
                self.user.transition_to(Deposit())
            elif cur_button == "transfer":
                self.user.transition_to(Transfer())
            elif cur_button == "exit":
                self.user.transition_to(StartMenu())

    def handle_message_text(self, msg: Message) -> None:

        pass
