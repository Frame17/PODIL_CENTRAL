from __future__ import annotations
from abc import ABC, abstractmethod
from telebot import TeleBot


from telebot.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    Message, CallbackQuery
)

from app.bot import texts


class StateBot(ABC, TeleBot):
    """ The StateBot defines the interface of interest to clients. It also maintains
        a reference to an instance of a State subclass, which represents the current
        state of the StateBot.
    """

    # A reference to the current state of the StateBot.
    _state = None

    def __init__(self, token: str, state: State) -> None:
        TeleBot.__init__(self, token=token, threaded=False)
        self.transition_to(state)

    def send_message(self, chat_id, text, disable_web_page_preview=None, reply_to_message_id=None, reply_markup=None,
                     parse_mode='HTML', disable_notification=None):

        """ Overwriting TeleBot father method to set default value param pars_mode to HTML
        """

        return super().send_message(chat_id, text, disable_web_page_preview, reply_to_message_id,
                                    reply_markup, parse_mode, disable_notification)

    def transition_to(self, state: State):
        """ The StateBot allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.state_bot = self

    """ The StateBot delegates part of its behavior to the current State object.
    """
    def request1(self, tg_id, msg_id, text='') -> Message:
        self.delete_message(tg_id, msg_id)
        msg = self._state.handle1(tg_id, msg_id, text)
        return msg


class State(ABC):
    """ The base State class declares methods that all Concrete State should
        implement and also provides a backreference to the StateBot object,
        associated with the State. This backreference can be used by States to
        transition the StateBot to another State.
    """

    @property
    def state_bot(self) -> StateBot:
        return self._state_bot

    @state_bot.setter
    def state_bot(self, state_bot: StateBot) -> None:
        self._state_bot = state_bot

    @abstractmethod
    def handle1(self, tg_id, msg_id, text) -> Message:
        pass


""" Concrete States implement various behaviors, associated with a state of the StateBot.
"""


class ConcreteStateA(State):
    def handle1(self, tg_id, msg_id, text) -> Message:
        buttons = InlineKeyboardMarkup()

        buttons.add(
            InlineKeyboardButton(
                text=texts.create_card_button,
                callback_data='create_card'
            ),
            InlineKeyboardButton(
                text=texts.choose_card_button,
                callback_data='choose_card'
            )
        )

        new_msg = self.state_bot.send_message(tg_id, text + texts.state_1, reply_markup=buttons)

        self.state_bot.transition_to(ConcreteStateB())
        return new_msg


class ConcreteStateB(State):
    def handle1(self, tg_id, msg_id, text) -> Message:

        print("ConcreteStateB handles request1.")

