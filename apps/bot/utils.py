from telegram import User
from typing import Union

from .models import User as DBUser


def build_mention(user: Union[User, DBUser]):
    user_mention = user.full_name
    if user.username:
        user_mention += f" (@{user.username})"
    return user_mention
