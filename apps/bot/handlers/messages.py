from .. import router
from ..models import User


@router.message("^@[a-zA-Z0-9_]{5,}$")
def handle_username(user, bot, chat, text):
    opponent_username = text[1:]  # remove @ symbol

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
        bot.sendMessage(chat.id, text)

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


# этот хендлер должен быть последним
@router.message("")
def handle_unknown_message(user, bot):
    message = f'Моя твоя не понимать\.\nНапиши /help, чтобы узнать, что я понимаю\.'
    bot.sendMessage(user.id, message, parse_mode="MarkdownV2")

