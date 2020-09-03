from . import registered
from .decorators import command_handlers, text_handlers

for handler_module in registered:
    __import__(handler_module)


def handle_message(message):
    if message.text.startswith("/"):
        for command_handler in command_handlers:
            command_handler(message)
    else:
        for text_handler in text_handlers:
            text_handler(message)
