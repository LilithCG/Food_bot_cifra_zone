from aiogram import types
from aiogram.utils.callback_data import CallbackData

cart_cb = CallbackData("Cart", "product_name", "action")

delivery_list_keyboard = types.InlineKeyboardMarkup(row_width=1)
delivery_list_keyboard.add(types.InlineKeyboardButton('Пицца Чеддер', callback_data='0'))
delivery_list_keyboard.add(types.InlineKeyboardButton('Китайская забегаловка', callback_data='1'))
delivery_list_keyboard.add(types.InlineKeyboardButton('Полёт', callback_data='2'))
delivery_list_keyboard.add(types.InlineKeyboardButton('Суши Wok', callback_data='3'))

pc_open_menu_keyboard = types.InlineKeyboardMarkup(row_width=1)
pc_open_menu_keyboard.add(types.InlineKeyboardButton('Открыть меню', callback_data='0m'))

creator_menu_keyboard = types.InlineKeyboardMarkup(row_width=1)
creator_menu_keyboard.add(types.InlineKeyboardButton('Открыть меню', callback_data='0m'))
creator_menu_keyboard.add(types.InlineKeyboardButton('Оформить заказ', callback_data='close_order'))
creator_menu_keyboard.add(types.InlineKeyboardButton('Удалить заказ', callback_data='delete_order'))

pc_category_menu = types.InlineKeyboardMarkup(row_width=2)
btn0 = types.InlineKeyboardButton('Пицца', callback_data='Пицца')
btn1 = types.InlineKeyboardButton('Бургеры', callback_data='Бургеры')
btn2 = types.InlineKeyboardButton('Роллы', callback_data='Роллы')
btn3 = types.InlineKeyboardButton('Сеты', callback_data='Сеты')
btn4 = types.InlineKeyboardButton('Суши', callback_data='Суши')
btn5 = types.InlineKeyboardButton('Лапша-Паста', callback_data='Лапша-Паста')
btn6 = types.InlineKeyboardButton('Супы', callback_data='Супы')
btn7 = types.InlineKeyboardButton('Салаты', callback_data='Салаты')
btn8 = types.InlineKeyboardButton('Закуски', callback_data='Закуски')
btn9 = types.InlineKeyboardButton('Десерты', callback_data='Десерты')
btn10 = types.InlineKeyboardButton('Напитки', callback_data='Напитки')
btn11 = types.InlineKeyboardButton('Соусы', callback_data='Соусы')
pc_category_menu.add(btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn7, btn9, btn10, btn11)
