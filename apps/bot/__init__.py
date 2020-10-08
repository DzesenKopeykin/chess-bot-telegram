from telegram.ext.updater import Updater, Dispatcher
from django.conf import settings


updater = Updater(settings.BOT_TOKEN, use_context=True)
dispatcher: Dispatcher = updater.dispatcher
