import os
from datetime import datetime
from pathlib import Path

import chess
import chess.svg
from cairosvg import svg2png
from django.conf import settings
from telegram import Chat, Message, Update, User
from telegram.ext import CallbackQueryHandler
from telegram.ext.callbackcontext import CallbackContext

from .. import dispatcher
from ..models import User as DBUser
from ..utils import build_mention


def handle_no_start_game_button(update: Update, context: CallbackContext) -> None:
    player: User = update.effective_user
    chat: Chat = update.effective_chat
    message: Message = update.effective_message
    opponent_id: str = update.callback_query.data.split("|")[1]
    opponent_db: DBUser = DBUser.objects.filter(id=opponent_id).first()

    context.bot.delete_message(chat_id=chat.id, message_id=message.message_id)
    player.send_message(f"Вы отказались от партии с {build_mention(opponent_db)}")
    context.bot.send_message(
        chat_id=opponent_db.id,
        text=f"{build_mention(player)} отказался играть с вами партию",
    )


def handle_yes_start_game_button(update: Update, context: CallbackContext) -> None:
    player: User = update.effective_user
    player_db: DBUser = DBUser.objects.filter(id=player.id).first()
    opponent_id: str = update.callback_query.data.split("|")[1]
    opponent_db: DBUser = DBUser.objects.filter(id=opponent_id).first()

    if not player_db or not opponent_db:
        player.send_message("Невозможно сыграть партию.")

    elif player_db.in_game:
        player.send_message("Сначала закончите текущую партию.")

    elif opponent_db.in_game:
        player.send_message(f"Ваш оппонент уже начал партию с другим игроком.")

    else:
        player_db.start_game(opponent_db)

        image_name = (
            f"{player_db.id}-{opponent_db.id}-"
            + str(datetime.timestamp(datetime.now())).split(".")[0]
            + ".png"
        )
        image_path = str(Path(settings.BASE_DIR, f"images/{image_name}"))
        svg2png(chess.svg.board(chess.Board()), write_to=image_path)

        context.bot.send_photo(chat_id=player.id, photo=open(image_path, "rb"))
        context.bot.send_photo(chat_id=opponent_id, photo=open(image_path, "rb"))

        os.remove(image_path)


dispatcher.add_handler(
    CallbackQueryHandler(handle_no_start_game_button, pattern="no_start_game")
)
dispatcher.add_handler(
    CallbackQueryHandler(handle_yes_start_game_button, pattern="yes_start_game")
)
