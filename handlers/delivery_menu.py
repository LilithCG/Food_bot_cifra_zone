import os

from aiogram import types
from aiogram.types import InputFile, CallbackQuery

from bot_creator import dp, bot
from keyboards.inline_keyboards import pc_category_menu, cart_cb
from keyboards.reply_keyboards import reply_back_keyboard, main_keyboard
from modules import database


@dp.callback_query_handler(text='0m')
async def inline_pc_category_callback_handler(query: types.CallbackQuery):
    await query.answer()
    await bot.send_message(query.from_user.id, "Пицца Чеддер", reply_markup=pc_category_menu)


@dp.callback_query_handler(text='Пицца')
@dp.callback_query_handler(text='Бургеры')
@dp.callback_query_handler(text='Роллы')
@dp.callback_query_handler(text='Сеты')
@dp.callback_query_handler(text='Суши')
@dp.callback_query_handler(text='Лапша-Паста')
@dp.callback_query_handler(text='Супы')
@dp.callback_query_handler(text='Салаты')
@dp.callback_query_handler(text='Закуски')
@dp.callback_query_handler(text='Десерты')
@dp.callback_query_handler(text='Напитки')
@dp.callback_query_handler(text='Соусы')
async def inline_pc_menu_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    await bot.send_message(query.from_user.id, text=answer_data, reply_markup=reply_back_keyboard)
    food_data = database.select_all_food_from_category(answer_data)
    for i in range(len(food_data)):
        answer_text = f"{food_data[i][1]}\n{food_data[i][2]}₽"
        photo_path = InputFile(f"parsers/pc_img/{food_data[i][3]}")
        add_to_basket_keyboard = types.InlineKeyboardMarkup(row_width=1)
        add_to_basket_keyboard.add(types.InlineKeyboardButton('Добавить', callback_data=cart_cb.new(product_name=food_data[i][0], action="add")))
        await bot.send_photo(chat_id=query.from_user.id, photo=photo_path, caption=answer_text, reply_markup=add_to_basket_keyboard)
    await query.answer()


@dp.callback_query_handler(cart_cb.filter(action=["add"]))
async def add_to_cart_handler(query: types.CallbackQuery, callback_data: dict):
    product_id = callback_data.get("product_name")
    database.insert_to_basket('1', query.from_user.id, database.get_product_name(product_id), product_id)
    await query.answer("Добавлено в корзину")


@dp.message_handler(text="🔙 Назад в меню")
async def back_menu_handler(message: types.Message):
    await message.answer("🔙", reply_markup=main_keyboard)
    await bot.send_message(message.chat.id, "Пицца Чеддер", reply_markup=pc_category_menu)

