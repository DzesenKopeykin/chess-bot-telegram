#!/usr/bin/env python
import django



if __name__ == "__main__":
    django.setup()

    # initialize updater
    from apps.bot import updater

    # initialize all handlers
    from apps.bot.handlers import *  # noqa

    print("Bot is running...")

    updater.start_polling()
    updater.idle()
