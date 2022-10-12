from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="🍴 Начать заказ"),
            KeyboardButton(text="📋 Текущий заказ"),
        ],
        [
            KeyboardButton(text="🛒 Корзина"),
        ],
    ]
)

reply_back_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[
        KeyboardButton(text="🔙 Назад в меню"),
        ],
    ]
)
