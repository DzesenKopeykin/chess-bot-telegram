import json
import traceback

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Bot, Chat, Message, User

from .handlers.base import handle_message


@csrf_exempt
def telegram_update(request, bot_token):
    if bot_token != settings.BOT_TOKEN:
        return HttpResponse("OK")

    data = json.loads(request.body)
    message_data = data["message"]
    bot = Bot(token=settings.BOT_TOKEN)

    if "text" not in message_data:
        return HttpResponse("OK")

    user = User(**message_data["from"])
    chat = Chat(**message_data["chat"])
    message = Message(
        message_id=message_data["message_id"],
        from_user=user,
        date=message_data["date"],
        chat=chat,
        bot=bot,
        text=message_data["text"],
    )

    if settings.DEBUG:
        try:
            handle_message(message)
        except Exception:
            traceback.print_exc()
    else:
        handle_message(message)

    return HttpResponse("OK")
