from aiogram import types

from bot_creator import dp, bot
from keyboards.inline_keyboards import cart_cb
from modules import database


@dp.message_handler(text="🛒 Корзина")
async def start_order_handler(message: types.Message):
    user_basket = database.select_basket_user(message.chat.id)
    sum = 0.0
    for i in range(len(user_basket)):
        price = database.select_price(user_basket[i][2])
        price = str(price)
        sum += float(price.replace(',', '.'))
        del_pos_keyboard = types.InlineKeyboardMarkup(row_width=1)
        del_pos_keyboard.add(types.InlineKeyboardButton('🗑 Удалить', callback_data=cart_cb.new(product_name=user_basket[i][0], action="delete")))
        await message.answer(text=f"{user_basket[i][1]}\n{price}₽", reply_markup=del_pos_keyboard)
    await message.answer(text=f"Сумма корзины: {sum}₽")


@dp.callback_query_handler(cart_cb.filter(action=["delete"]))
async def add_to_cart_handler(query: types.CallbackQuery, callback_data: dict):
    product_name = callback_data.get("product_name")
    database.delete_product_from_basket(order_id=1, chat_id=query.from_user.id, product_id=product_name)
    await query.answer("Удалено из корзины")
