import re


class BaseRegistry:
    def __init__(self):
        self.handlers = {}

    def register(self, key, handler):
        self.handlers[key] = handler

    def _get(self, key):
        return self.handlers.get(key)


class MessageRegistry(BaseRegistry):
    def get(self, update_data):
        for regex in self.handlers.keys():
            match = re.search(regex, update_data["message"]["text"])
            if match:
                return self._get(regex)


class CommandRegistry(BaseRegistry):
    def get(self, update_data):
        return self._get(update_data["message"]["text"])


class EditedMessageRegistry(BaseRegistry):
    def get(self, update_data):
        # TODO: investigate which key can use here
        pass


class ChannnelPostRegistry(BaseRegistry):
    def get(self, update_data):
        # TODO: investigate which key can use here
        pass


class EditedChannelPostRegistry(BaseRegistry):
    def get(self, update_data):
        # TODO: investigate which key can use here
        pass


class InlineQueryRegistry(BaseRegistry):
    def get(self, update_data):
        # TODO: investigate which key can use here
        pass


class ChosenInlineResultRegistry(BaseRegistry):
    def get(self, update_data):
        # TODO: investigate which key can use here
        pass


class CallbackQueryRegistry(BaseRegistry):
    def get(self, update_data):
        # TODO: investigate which key can use here
        pass


class ShippingQueryRegistry(BaseRegistry):
    def get(self, update_data):
        # TODO: investigate which key can use here
        pass


class PreCheckoutQueryRegistry(BaseRegistry):
    def get(self, update_data):
        # TODO: investigate which key can use here
        pass


class PollRegistry(BaseRegistry):
    def get(self, update_data):
        # TODO: investigate which key can use here
        pass


class PollAnswerRegistry(BaseRegistry):
    def get(self, update_data):
        # TODO: investigate which key can use here
        pass
