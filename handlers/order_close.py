from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from modules import sel_system, database

from bot_creator import dp, bot


class Order_end(StatesGroup):
    choosing_phone = State()
    choosing_fio = State()
    choosing_street = State()
    choosing_house = State()
    choosing_comment = State()

phone = ''
fio = ''
street = ''
house = ''
comment = ''


@dp.callback_query_handler(text='close_order')
async def inline_close_order_callback_handler(query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(query.from_user.id, text="Введите ваш номер телефона")
    await state.set_state(Order_end.choosing_phone)
    await query.answer()


@dp.message_handler(state=Order_end.choosing_phone)
async def phone_state_command(message: types.Message, state: FSMContext):
    global phone
    if len(message.text) != 11:
        await message.reply('Пожалуйста введите корректный номер телефона, 11 цифр без знака +')
    else:
        phone = message.text
        await state.set_state(Order_end.choosing_fio)
        await message.reply('Введите ФИО')


@dp.message_handler(state=Order_end.choosing_fio)
async def fio_state_command(message: types.Message, state: FSMContext):
    global fio
    fio = message.text
    await state.set_state(Order_end.choosing_street)
    await message.reply('Введите название улицы')


@dp.message_handler(state=Order_end.choosing_street)
async def street_state_command(message: types.Message, state: FSMContext):
    global street
    street = message.text
    await state.set_state(Order_end.choosing_house)
    await message.reply('Введите номер дома')


@dp.message_handler(state=Order_end.choosing_house)
async def house_state_command(message: types.Message, state: FSMContext):
    global house
    house = message.text
    await state.set_state(Order_end.choosing_comment)
    await message.reply('Введите коментарий к заказу (необязательно)')


@dp.message_handler(state=Order_end.choosing_comment)
async def house_state_command(message: types.Message, state: FSMContext):
    global comment
    comment = message.text
    await state.set_state(None)
    basket = database.select_all_basket()
    text = f"Телефон: {phone}\nФИО: {fio}\nУлица: {street}\nДом: {house}\nКоментарий к заказу: {comment}\n\n"
    sum = 0.0
    for pos in basket:
        ref = database.select_ref(pos[0])
        price = database.select_price(pos[2])
        price = str(price)
        sum += float(price.replace(',', '.'))
        text += f"{ref} {pos[1]} {price}₽\n"
    text += f"Общая сумма заказа: {sum}₽"
    end_keyboard = types.InlineKeyboardMarkup(row_width=1)
    end_keyboard.add(types.InlineKeyboardButton('Отправить заказ в доставку', callback_data='delivery_go'))
    end_keyboard.add(types.InlineKeyboardButton('Изменить данные доставки', callback_data='close_order'))
    end_keyboard.add(types.InlineKeyboardButton('Удалить заказ', callback_data='delete_order'))
    await message.reply(text, reply_markup=end_keyboard)


@dp.callback_query_handler(text='delivery_go')
async def send_to_delivery_callback_handler(query: types.CallbackQuery):
    # Отправка в Selenium
    our_basket = database.select_all_basket()
    links = []
    for pos in our_basket:
        links.append(database.select_link(pos[2]))
    sel_system.launch(links, phone=phone, fio=fio, street=street, house=house, comment=comment)
    await bot.send_message(query.from_user.id, text="Заказ успешно отправлен в доставку")
    basket_list = database.select_all_basket()
    chat_id_list = []
    for pos in basket_list:
        if pos[0] not in chat_id_list:
            chat_id_list.append(pos[0])
    for chat_id in chat_id_list:
        user_basket = database.select_basket_user(chat_id)
        sum = 0.0
        for i in range(len(user_basket)):
            price = database.select_price(user_basket[i][2])
            price = str(price)
            sum += float(price.replace(',', '.'))
        await bot.send_message(chat_id, text=f"Ваш заказ был отправлен в доставку\nСтоимость вашего заказа: {sum}₽\nТелефон для перевода: +{phone}")
    database.delete_all_basket()
    database.close_order()
    await query.answer()



@dp.callback_query_handler(text='delete_order')
async def delete_order_callback_handler(query: types.CallbackQuery):
    database.delete_all_basket()
    database.close_order()
    await query.answer()
    await bot.send_message(query.from_user.id, text="Заказ полностью удален")