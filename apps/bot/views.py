import json
import traceback

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Bot, Update

from . import dispatcher

# initialize all handlers
from .handlers import *  # noqa


@csrf_exempt
def telegram_update(request: HttpRequest, bot_token: str) -> HttpResponse:
    if bot_token != settings.BOT_TOKEN:
        return HttpResponse("OK")

    bot = Bot(settings.BOT_TOKEN)
    update_data: str = json.loads(request.body)
    update = Update.de_json(update_data, bot)

    try:
        dispatcher.process_update(update)
    except Exception:
        traceback.print_exc()

    return HttpResponse("OK")
