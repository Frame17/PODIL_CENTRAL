from . import telegram


@telegram.route('/')
def hello():
    return 'Hello world', 200
