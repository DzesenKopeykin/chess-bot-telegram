from telegram import InlineKeyboardButton, InlineKeyboardMarkup, User

from ..models import User as DBUser


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
        user_mention = self.player.full_name
        if self.player.username:
            user_mention += f" (@{self.player.username})"

        return (
            f"Здравствуйте, {self.opponent_db.first_name}!\n"
            f"{user_mention} предлагает сыграть в шахматы. Вы согласны?"
        )

    def _build_keyboard(self) -> InlineKeyboardMarkup:
        yes_button = InlineKeyboardButton(
            "Да \U0001f44c", callback_data="yes_start_game"
        )
        no_button = InlineKeyboardButton("Нет", callback_data="no_start_game")
        return InlineKeyboardMarkup([[yes_button, no_button]])
