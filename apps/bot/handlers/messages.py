from .decorators import text_handler
from ..models import User


@text_handler("^@[a-zA-Z0-9_]{5,}$")
def handle_username(message, match):
    opponent_username = match[1:]  # remove @ symbol
    player = message.from_user

    if opponent_username == player.username:
        text = "Вы не можете начать партию с собой."
        message.bot.sendMessage(player.id, text)
        return

    opponent = User.objects.filter(username=opponent_username).first()

    if not opponent:
        text = (
            "ChessBot не знает этого пользователя \u200d."
            "Возможно он не открывал этого бота. Для того чтобы узнать более "
            "подробную информацию о том что требуется, чтобы "
            "начать партию используйте команду /help_how_to_start."
        )
        message.bot.sendMessage(message.chat.id, text)

    else:
        player_mention = player.full_name
        if player.username:
            player_mention += f" (@{player.username})"
        text = (
            f"Здравствуйте, {opponent.first_name}! {player_mention} "
            "предлагает сыграть в шахматы. Вы согласны?"
        )
        message.bot.sendMessage(opponent.id, text)

        text = (
            f"Я отправил ваше предложение @{opponent.username}. "
            "Партия начнётся когда он(а) согласится."
        )
        message.bot.sendMessage(player.id, text)
