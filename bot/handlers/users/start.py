from aiogram import types
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

from bot.loader import dp, MainState


@dp.message_handler(commands=["start"], state="*")
async def start(message: types.Message):
    await MainState.phone_number.set()

    await message.answer(
        text=f"Assalomu alaykum {message.from_user.full_name}!",
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton(text="Send phone number!", request_contact=True)]],
            resize_keyboard=True,
        ),
    )
