from __future__ import annotations

import json
import os
from abc import ABC, abstractmethod

import requests
from telebot.types import CallbackQuery, Message


class User(object):
    _state = None
    _cur_card: int = None

    def __init__(self, tg_id, f_name, l_name, state: UserState) -> None:
        self.tg_id = tg_id
        self.f_name = f_name
        self.l_name = l_name
        self.transition_to(state)

    def transition_to(self, state: UserState) -> None:
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.user = self
        self._state.send_menu()

    def command_request(self, msg: Message):
        self._state.handle_command(msg)

    def button_request(self, call: CallbackQuery):
        self._state.handle_button(call)

    def message_text_request(self, msg: Message):
        self._state.handle_message_text(msg)

    @property
    def cur_card(self):
        return self._cur_card

    @cur_card.setter
    def cur_card(self, value):
        self._cur_card = value

    def get_balance(self):
        r = requests.get(os.getenv("SERVER_URL") + "balance?id=" + self.cur_card)
        return json.loads(r.content)

    def do_withdraw(self, amount):
        data = {
            "cardId": self.cur_card,
            "amount": amount
        }
        r = requests.post(os.getenv("SERVER_URL") + "withdraw", json=data)
        print(r.content)
        return json.loads(r.content)

    def do_deposit(self, amount):
        data = {
            "cardId": self.cur_card,
            "amount": amount
        }
        r = requests.post(os.getenv("SERVER_URL") + "deposit", json=data)
        print(r.content)
        return json.loads(r.content)

    def do_card_auth(self, pin):
        data = {
            "cardId": self.cur_card,
            "pin": pin
        }
        r = requests.post(os.getenv("SERVER_URL") + "auth", json=data)
        print(r.content)
        return json.loads(r.content)



class UserState(ABC):

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, user: User) -> None:
        self._user = user

    @abstractmethod
    def send_menu(self) -> None:
        pass

    @abstractmethod
    def handle_command(self, msg: Message) -> None:
        pass

    @abstractmethod
    def handle_button(self, call: CallbackQuery) -> None:
        pass

    @abstractmethod
    def handle_message_text(self, msg: Message) -> None:
        pass
