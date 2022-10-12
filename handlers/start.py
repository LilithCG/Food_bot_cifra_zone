from aiogram.types import Message

from bot_creator import dp
from keyboards.reply_keyboards import main_keyboard
from modules import database


@dp.message_handler(commands=["start"])
async def start(message: Message):
    try:
        database.insert_user(chat_id=message.chat.id, name=message.chat.first_name, ref=f"@{message.chat.username}")
    except:
        await message.reply(f"Добро пожаловать {message.chat.first_name}", reply_markup=main_keyboard)
    else:
        await message.reply(f"Добро пожаловать", reply_markup=main_keyboard)
