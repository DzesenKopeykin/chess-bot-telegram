from .decorators import processed_message_update_data
from .registries import (
    CallbackQueryRegistry,
    ChannnelPostRegistry,
    ChosenInlineResultRegistry,
    CommandRegistry,
    EditedChannelPostRegistry,
    EditedMessageRegistry,
    InlineQueryRegistry,
    MessageRegistry,
    PollAnswerRegistry,
    PollRegistry,
    PreCheckoutQueryRegistry,
    ShippingQueryRegistry,
)


class UpdateRouter:
    def __init__(self):
        self.message_registry = MessageRegistry()
        self.command_registry = CommandRegistry()
        self.edited_message_registry = EditedMessageRegistry()
        self.channel_post_registry = ChannnelPostRegistry()
        self.edited_channel_post_registry = EditedChannelPostRegistry()
        self.inline_query_registry = InlineQueryRegistry()
        self.chosen_inline_result_registry = ChosenInlineResultRegistry()
        self.callback_query_registry = CallbackQueryRegistry()
        self.shipping_query_registry = ShippingQueryRegistry()
        self.pre_checkout_query_registry = PreCheckoutQueryRegistry()
        self.poll_registry = PollRegistry()
        self.poll_answer_registry = PollAnswerRegistry()

    def message(self, regex):
        return self._register_handler(regex, self.message_registry)

    def command(self, command):
        return self._register_handler(command, self.command_registry)

    def edited_message(self, key):  # TODO: investigate which key can use here
        return self._register_handler(key, self.edited_message_registry)

    def channel_post(self, key):  # TODO: investigate which key can use here
        return self._register_handler(key, self.channel_post_registry)

    def edited_channel_post(self, key):  # TODO: investigate which key can use here
        return self._register_handler(key, self.edited_channel_post_registry)

    def inline_query(self, key):  # TODO: investigate which key can use here
        return self._register_handler(key, self.chosen_inline_result_registry)

    def chosen_inline_result(self, key):  # TODO: investigate which key can use here
        return self._register_handler(key, self.chosen_inline_result_registry)

    def callback_query(self, key):  # TODO: investigate which key can use here
        return self._register_handler(key, self.callback_query_registry)

    def shipping_query(self, key):  # TODO: investigate which key can use here
        return self._register_handler(key, self.shipping_query_registry)

    def pre_checkout_query(self, key):  # TODO: investigate which key can use here
        return self._register_handler(key, self.pre_checkout_query_registry)

    def poll(self, key):  # TODO: investigate which key can use here
        return self._register_handler(key, self.poll_registry)

    def poll_answer(self, key):  # TODO: investigate which key can use here
        return self._register_handler(key, self.poll_answer_registry)

    def route(self, update_data):
        handler = None

        if "message" in update_data:
            handler = self.command_registry.get(update_data)
            if not handler:
                handler = self.message_registry.get(update_data)
            handler = processed_message_update_data(handler)

        elif "edited_message" in update_data:
            handler = self.edited_message_registry.get(update_data)

        elif "channel_post" in update_data:
            handler = self.channel_post_registry.get(update_data)

        elif "edited_channel_post" in update_data:
            handler = self.edited_channel_post_registry.get(update_data)

        elif "inline_query" in update_data:
            handler = self.inline_query_registry.get(update_data)

        elif "chosen_inline_result" in update_data:
            handler = self.chosen_inline_result_registry.get(update_data)

        elif "callback_query" in update_data:
            handler = self.callback_query_registry.get(update_data)

        elif "shipping_query" in update_data:
            handler = self.shipping_query_registry.get(update_data)

        elif "pre_checkout_query" in update_data:
            handler = self.pre_checkout_query_registry.get(update_data)

        elif "poll" in update_data:
            handler = self.poll_registry.get(update_data)

        elif "poll_answer" in update_data:
            handler = self.poll_answer_registry.get(update_data)

        return handler(update_data)

    def _register_handler(self, key, registry):
        def wrapper(handler):
            registry.register(key, handler)
            return handler

        return wrapper
