from aiogram import types

from bot_creator import dp


@dp.message_handler(text="📝 История заказов")
async def with_puree(message: types.Message):
    await message.reply("Показываю историю заказов")