import inspect

from django.conf import settings
from telegram import Bot, Chat, Message, User


def processed_message_update_data(handler):
    def wrapper(update_data):
        kwargs = {}
        arg_names = inspect.signature(handler).parameters

        if "update_id" in arg_names:
            kwargs["update_id"] = update_data["update_id"]

        if "bot" in arg_names:
            kwargs["bot"] = Bot(token=settings.BOT_TOKEN)

        message_data = update_data["message"]

        if "text" in arg_names:
            kwargs["text"] = message_data["text"]

        if "user" in arg_names:
            kwargs["user"] = User(**message_data["from"])

        if "chat" in arg_names:
            kwargs["chat"] = Chat(**message_data["chat"])

        if "message" in arg_names:
            kwargs["message"] = Message(
                message_id=message_data["message_id"],
                from_user=kwargs.get("user") or User(**message_data["from"]),
                date=message_data["date"],
                chat=kwargs.get("chat") or Chat(**message_data["chat"]),
                bot=kwargs.get("bot") or Bot(token=settings.BOT_TOKEN),
                text=message_data["text"],
            )

        return handler(**kwargs)

    return wrapper
