import json
import traceback

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Bot, Update

from . import dispatcher
from .handlers import *  # noqa


@csrf_exempt
def telegram_update(request, bot_token):
    if bot_token != settings.BOT_TOKEN:
        return HttpResponse("OK")

    update_data = json.loads(request.body)
    bot = Bot(settings.BOT_TOKEN)
    update = Update.de_json(update_data, bot)

    if settings.DEBUG:
        from pprint import pprint
        pprint(update_data)

    if settings.DEBUG:
        try:
            dispatcher.process_update(update)
        except Exception:
            traceback.print_exc()
    else:
        dispatcher.process_update(update)

    return HttpResponse("OK")
