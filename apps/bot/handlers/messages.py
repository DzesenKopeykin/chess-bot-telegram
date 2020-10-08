from telegram import MessageEntity, Update
from telegram.ext import Filters, MessageHandler
from telegram.ext.callbackcontext import CallbackContext

from .. import dispatcher
from ..models import User


def handle_username_message(update: Update, context: CallbackContext):
    user, message, bot = update.effective_user, update.effective_message, context.bot
    opponent_username = message.text[1:]  # remove @ symbol

    if opponent_username == user.username:
        text = "Вы не можете начать партию с собой."
        bot.sendMessage(user.id, text)
        return

    opponent = User.objects.filter(username=opponent_username).first()

    if not opponent:
        text = (
            "ChessBot не знает этого пользователя."
            "Возможно он не открывал этого бота. "
            "Используйте команду /help_how_to_start чтобы узнать больше."
        )
        bot.sendMessage(message.chat.id, text)

    else:
        user_mention = user.full_name
        if user.username:
            user_mention += f" (@{user.username})"
        text = (
            f"Здравствуйте, {opponent.first_name}! {user_mention} "
            "предлагает сыграть в шахматы. Вы согласны?"
        )
        bot.sendMessage(opponent.id, text)

        text = (
            f"Я отправил ваше предложение @{opponent.username}. "
            "Партия начнётся когда он(а) согласится."
        )
        bot.sendMessage(user.id, text)


def handle_unknown_message(update: Update, context: CallbackContext):
    message = f"Моя твоя не понимать\.\nНапиши /help, чтобы узнать, что я понимаю\."
    context.bot.sendMessage(update.effective_user.id, message, parse_mode="MarkdownV2")


filters_for_username = Filters.text & Filters.entity(MessageEntity.MENTION)
filters_for_any_message = Filters.all

dispatcher.add_handler(MessageHandler(filters_for_username, handle_username_message))
dispatcher.add_handler(MessageHandler(filters_for_any_message, handle_unknown_message))
