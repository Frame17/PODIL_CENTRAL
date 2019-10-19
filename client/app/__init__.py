import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    # app.config.from_object(os.getenv("APP_SETTINGS", 'config.DevConfig'))

    from . bot import telegram

    app.register_blueprint(telegram)

    return app
