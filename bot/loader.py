import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from settings import BOT_TOKEN

loop = asyncio.get_event_loop()

bot = Bot(token=BOT_TOKEN, loop=loop)
storage = JSONStorage(path="storage.json")
dp = Dispatcher(bot=bot, storage=storage)


class MainState(StatesGroup):
    phone_number = State()
    gender = State()
