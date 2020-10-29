from telegram import InlineKeyboardButton, InlineKeyboardMarkup, User

from ..models import User as DBUser
from ..utils import build_mention


class BaseMessage:
    def build(self):
        return dict(text=self._build_text(), reply_markup=self._build_keyboard_markup())

    def _build_text(self) -> str:
        pass

    def _build_keyboard_markup(self) -> InlineKeyboardMarkup:
        pass


class AskStartGameMessage(BaseMessage):
    def __init__(self, player: User, opponent_db: DBUser) -> None:
        self.player: User = player
        self.opponent_db: DBUser = opponent_db

    def _build_text(self) -> str:
        return (
            f"Здравствуйте, {self.opponent_db.first_name}!\n"
            f"{build_mention(self.player)} предлагает сыграть в шахматы. Вы согласны?"
        )

    def _build_keyboard_markup(self) -> InlineKeyboardMarkup:
        yes_button = InlineKeyboardButton(
            "Да \U0001f44c", callback_data=f"yes_start_game|{self.player.id}"
        )
        no_button = InlineKeyboardButton(
            "Нет", callback_data=f"no_start_game|{self.player.id}"
        )
        return InlineKeyboardMarkup([[yes_button, no_button]])
