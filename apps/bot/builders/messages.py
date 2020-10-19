from telegram import InlineKeyboardButton, InlineKeyboardMarkup, User

from ..models import User as DBUser
from ..utils import build_mention


class BaseMessage:
    def __init__(self):
        self.text: str = self._build_text()
        self.keyboard: InlineKeyboardMarkup = self._build_keyboard()

    def _build_text(self) -> str:
        raise NotImplementedError

    def _build_keyboard(self) -> InlineKeyboardMarkup:
        pass


class AskStartGameMessage(BaseMessage):
    def __init__(self, player: User, opponent_db: DBUser) -> None:
        self.player: User = player
        self.opponent_db: DBUser = opponent_db
        super().__init__()

    def _build_text(self) -> str:
        return (
            f"Здравствуйте, {self.opponent_db.first_name}!\n"
            f"{build_mention(self.player)} предлагает сыграть в шахматы. Вы согласны?"
        )

    def _build_keyboard(self) -> InlineKeyboardMarkup:
        yes_button = InlineKeyboardButton(
            "Да \U0001f44c", callback_data=f"yes_start_game|{self.player.id}"
        )
        no_button = InlineKeyboardButton(
            "Нет", callback_data=f"no_start_game|{self.player.id}"
        )
        return InlineKeyboardMarkup([[yes_button, no_button]])
