from telegram import Update, User, Message, Chat
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
    pass


dispatcher.add_handler(
    CallbackQueryHandler(handle_no_start_game_button, pattern="no_start_game")
)
dispatcher.add_handler(
    CallbackQueryHandler(handle_yes_start_game_button, pattern="yes_start_game")
)
