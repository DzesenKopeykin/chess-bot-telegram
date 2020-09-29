import json
import traceback

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import router
from .handlers import *  # noqa


@csrf_exempt
def telegram_update(request, bot_token):
    if bot_token != settings.BOT_TOKEN:
        return HttpResponse("OK")

    update_data = json.loads(request.body)

    from pprint import pprint
    pprint(update_data)

    if settings.DEBUG:
        try:
            router.route(update_data)
        except Exception:
            traceback.print_exc()
    else:
        router.route(update_data)

    return HttpResponse("OK")
