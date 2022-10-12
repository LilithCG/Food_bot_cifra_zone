from bot_creator import bot
from modules import database


def alert_new_order(creator_name, delivery_name):
    chat_id_list = database.select_all_users()
    for chat_id in chat_id_list:
        bot.send_message(chat_id, f'@{creator_name} создал новый заказ из доставки {delivery_name}')
