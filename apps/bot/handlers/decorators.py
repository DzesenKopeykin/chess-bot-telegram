from functools import wraps
import re

text_handlers = []
command_handlers = []


def text_handler(regex):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            message = args[0]
            match = re.search(regex, message.text)
            if match:
                kwargs["match"] = match[0]
                return func(*args, **kwargs)

        text_handlers.append(wrapper)
        return wrapper

    return decorator


def command_handler(command):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            message = args[0]
            if message.text == command:
                return func(*args, **kwargs)

        command_handlers.append(wrapper)
        return wrapper

    return decorator
