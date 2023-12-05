from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.loader import dp, MainState
from bot.filters.filters import gender_cb


@dp.callback_query_handler(state=MainState.gender)
async def gender(
    callback_query: types.CallbackQuery,
    state: FSMContext,
):
    await callback_query.answer()
    gender = gender_cb.parse(callback_query.data)

    await callback_query.message.delete()

    async with state.proxy() as data:
        await callback_query.message.answer(
            text=f"Thanks!\n\nPhone number: %s\nGender: %s"
            % (data["phone_number"], gender["value"]),
            reply_markup=types.ReplyKeyboardRemove(),
        )

        await MainState.first()
