from aiogram import types

from bot_creator import dp, bot
from keyboards.inline_keyboards import delivery_list_keyboard, pc_open_menu_keyboard, creator_menu_keyboard
from modules import database

menu_keyboard = None

@dp.message_handler(text="🍴 Начать заказ")
async def start_order_handler(message: types.Message):
    if len(database.select_all_current_orders()) == 0:
        await message.reply("Выберите ресторан:", reply_markup=delivery_list_keyboard)
    else:
        await message.reply("Заказ уже создан")


@dp.message_handler(text="📋 Текущий заказ")
async def current_order_handler(message: types.Message):
    global menu_keyboard

    text = ""
    current_orders = database.select_all_current_orders()
    if len(current_orders) != 0:
        text += f"Ресторан: {current_orders[0][3]}\nСоздатель: @{current_orders[0][2]}\n\n"
        if message.chat.id == current_orders[0][1]:
            await message.reply(text, reply_markup=creator_menu_keyboard)
        else:
            await message.reply(text, reply_markup=menu_keyboard)
    else:
        await message.reply("Пока никто не создал заказ")


# Выбор ресторана
@dp.callback_query_handler(text='0')
@dp.callback_query_handler(text='1')
@dp.callback_query_handler(text='2')
@dp.callback_query_handler(text='3')
async def inline_choose_delivery_callback_handler(query: types.CallbackQuery):
    global menu_keyboard
    answer_data = query.data
    alert_text = 'Hello'
    if answer_data == '0':
        database.insert_order(1, query.from_user.id, query.from_user.username, 'Пицца Чеддер', 'pizza_cheddar',
                              'new')
        alert_text = f'@{query.from_user.username} создал новый заказ из доставки Пицца Чеддер'
        menu_keyboard = pc_open_menu_keyboard
    elif answer_data == '1':
        return await query.answer(text='Доставка из этого ресторана скоро заработает')
    elif answer_data == '2':
        return await query.answer(text='Доставка из этого ресторана скоро заработает')
    elif answer_data == '3':
        return await query.answer(text='Доставка из этого ресторана скоро заработает')

    await query.answer(text='Заказ успешно создан')
    chat_id_list = database.select_all_users()
    for chat_id in chat_id_list:
        await bot.send_message(chat_id[0], alert_text, reply_markup=menu_keyboard)


