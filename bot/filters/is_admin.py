from aiogram import types
from aiogram.dispatcher.filters import Filter

from settings import ADMINS


class IsAdmin(Filter):
    key = "is_admin"

    async def check(self, message: types.Message) -> bool:
        return message.from_user.id in ADMINS
