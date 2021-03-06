from app.telegram.user.User import User


class Users(object):
    def __init__(self):
        self._users = []

    def add_user(self, user: User):
        self._users.append(user)

    def get_user_by_tg_id(self, tg_id):
        return next((user for user in self._users if user.tg_id == tg_id), None)
