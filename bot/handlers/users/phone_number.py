from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from bot.loader import dp, MainState


@dp.message_handler(
    state=MainState.phone_number, content_types=types.ContentType.CONTACT
)
async def phone_number(message: types.Message, state: FSMContext):
    await message.answer(
        text="Jinsingizni tanlang!",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="MALE", callback_data="gender:male")],
                [InlineKeyboardButton(text="FEMALE", callback_data="gender:female")],
            ],
        ),
    )
