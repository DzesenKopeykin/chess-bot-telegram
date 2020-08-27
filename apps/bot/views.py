import json

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def telegram_update(request, bot_token):
    if bot_token != settings.BOT_TOKEN:
        return HttpResponse("OK")

    data = json.loads(request.body)

    return HttpResponse("OK")
