from flask import Blueprint


telegram = Blueprint('telegram', __name__)

from . import web_hook
